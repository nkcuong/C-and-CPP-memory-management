	/* 
	* This program demonstrates the usage of shared memory in C++.
	* It creates a shared memory object, writes strings to it,
	* and maps the shared memory object to a pointer.
	From Operating System Concepts - 10 ed. by Abraham Silberschatz, Greg Gagne, and Peter Baer Galvin
	pages 133-134
	*/

#include <iostream>
#include <string>
#include <fcntl.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <unistd.h>

int main()
{


	/* the size (in bytes) of shared memory object */
	const int SIZE = 4096;
	/* name of the shared memory object */
	const char *name = "OS";
	/* strings written to shared memory */
	#include <iostream>
	#include <cstdio> // Add this line for snprintf



	/* shared memory file descriptor */
	#include <string> // Add this line for the missing include directive

	int fd;
	/* pointer to shared memory object */
	#include <cstring> // Add this line for the missing include directive

	char *ptr, *ptr1, *ptr2;
	std::string input_str;

	/* create the shared memory object */
	fd = shm_open(name, O_CREAT | O_RDWR, 0666);
	/* configure the size of the shared memory object */
	ftruncate(fd, SIZE);
	/* memory map the shared memory object */
	ptr = (char *)mmap(0, SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);

	while (1) {
		std::cout << "Enter a string: ";
		std::cin >> input_str;
		if (input_str == "exit") {
			break;
		}
		else {
			snprintf(ptr, SIZE, "%s", input_str.c_str());
			std::cout << ptr << std::endl;
		}
	}
	

	
	

	// shm_unlink(name);


	return 0;
}