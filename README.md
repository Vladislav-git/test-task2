Task:
1. Create a VirtualBox machine, install Ubuntu 18.04 there.

2. Initialise a private git repository on BitBucket and use it for storing the changes relevant to the task.

3. Start a Django-based web application, run it on local in the VM with the help of NginX/Gunicorn web server.

4. Use PostgreSQL as database management system.
5. Set the following functionality for the application:
- implement a hierarchy of classes which includes a base abstract class with multiple descendant classes implementing the functionality
- the clases should implement methods demonstrating various sorting algorithms, the required are Bubble, Insertion, and Merge sorts, any other would be a plus
- create a decorator which measures execution time for a decorated function, use it to decorate the sorting methods of classes
- set a simple Django model representing executions of the algorithms
- add the model to the Django admin section, allow filtering by algorithm type, and enable search and sorting by any model field
- create a simple Django view containing a form which allows to choose an algorithm, pick a file with unsorted integers, and execute the sorting (a record in the databse has to be created upon completion)
6. Demonstrate the results. 
