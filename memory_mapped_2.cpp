	/* 
	* This program demonstrates the usage of shared memory in C++.
	* It maps the shared memory object to a pointer and reads from it.
	Run the memory_mapped.cpp program first.
	From Operating System Concepts - 10 ed. by Abraham Silberschatz, Greg Gagne, and Peter Baer Galvin
	pages 133-134
	*/

#include <iostream>
#include <fcntl.h>
#include <sys/stat.h>
#include <sys/mman.h>
#include <unistd.h>

int main()
{
	/* the size (in bytes) of shared memory object */
	const int SIZE = 4096;
	/* name of the shared memory object */
	const char *name = "OS";
	/* shared memory file descriptor */
	int fd;
	/* pointer to shared memory obect */
	char *ptr;
	/* open the shared memory object */
	fd = shm_open(name, O_RDONLY, 0666);
	if (fd == -1) {
		perror("shm_open");
		return 1;
	}
	/* memory map the shared memory object */
	ptr = (char *)mmap(0, SIZE, PROT_READ, MAP_SHARED, fd, 0);
	if (ptr == MAP_FAILED) {
		perror("mmap");
		return 1;
	}

/* read from the shared memory object */
	// run until the shared memory object does not start with "H"
	while (ptr[0] != 'q') {
		std::cout << ptr << std::endl;
		sleep(1);
	}
	
	/* remove the shared memory object */
	shm_unlink(name);

	return 0;
}