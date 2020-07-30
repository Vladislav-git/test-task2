from django.shortcuts import render
from .models import NumberList
from abc import ABCMeta, abstractmethod
# import timeit



def form_view(request):
	file_lst = []
	lst = []
	result = []
	response = {}
	#////////
	if request.method == 'POST':
		numbers = request.POST['numbers']
		algorithm = request.POST['algorithm']
		file = request.FILES
		#//////
		if numbers != '' and file != {}:
			response = {'text':'Only one field required'}
			return render(request, 'index.html', response)
		#//////
		if request.FILES:
			file_data = request.FILES['myfile'].read().decode('utf-8')
			file_numbers = [int(x) for x in file_data.split(', ')]
			file_lst = file_numbers.copy()
			if algorithm == 'BubleSort':
				sort_b = BubleSort()
				result = sort_b.sort(file_numbers)
			if algorithm == 'InsertionSort':
				sort_i = InsertionSort()
				result = sort_i.sort(file_numbers)
			if algorithm == 'MergeSort':
				sort_m = MergeSort(file_numbers)
				result = sort_m.sort(file_numbers)
			NumberList.objects.create(algorithm=algorithm, number_list=file_lst, sorted_list=result)
			response = {
				'numbers':file_lst,
				'sorted_list':result
			}
			return render(request, 'index.html', response)
		#//////
		if numbers != '':
			lst = [int(x) for x in numbers.split(', ')]
			lst1 = lst.copy()
			if algorithm == 'BubleSort':
				sort_b = BubleSort()
				result = sort_b.sort(lst1)
			if algorithm == 'InsertionSort':
				sort_i = InsertionSort()
				result = sort_i.sort(lst1)
			if algorithm == 'MergeSort':
				sort_m = MergeSort()
				result = sort_m.sort(lst1)
			NumberList.objects.create(algorithm=algorithm, number_list=lst, sorted_list=result)
			response = {
				'numbers':lst,
				'sorted_list':result
			}
	return render(request, 'index.html', response)

# sorting

class Basic():
	__metaclass__ = ABCMeta
	@abstractmethod
	def sort(self, arr):
		pass


class BubleSort(Basic):
	def sort(self, arr):
		n = len(arr)

		for i in range(n):
			swapped = False

			for j in range(0, n - i - 1):

				if arr[j] > arr[j + 1]:
					arr[j], arr[j + 1] = arr[j + 1], arr[j]
					swapped = True

			if swapped == False:
				break
		return arr

class InsertionSort(Basic):
	def sort(self, arr):

		for i in range(1, len(arr)):
			key = arr[i]
			j = i - 1

			while j >= 0 and key < arr[j]:
				arr[j + 1] = arr[j]
				j -= 1

			arr[j + 1] = key
		return arr


class MergeSort():
	def sort(self,arr):

		if len(arr) > 1:
			mid = len(arr) // 2
			L = arr[:mid]
			R = arr[mid:]

			self.sort(L)
			self.sort(R)

			i = j = k = 0

			while i < len(L) and j < len(R):
				if L[i] < R[j]:
					arr[k] = L[i]
					i += 1
				else:
					arr[k] = R[j]
					j += 1
				k += 1

			while i < len(L):
				arr[k] = L[i]
				i += 1
				k += 1

			while j < len(R):
				arr[k] = R[j]
				j += 1
				k += 1
		return arr


#////////////////////////////////////////////////
# if u need to use decorator uncomment code below(with import timeit) and insert @func_time before def

# def func_time(func):
# 	def wrapper(self,arr):
# 		start_time = timeit.default_timer()
# 		func(self,arr)
# 		result_time = timeit.default_timer() - start_time
# 		print('Function "{name}" took {time} seconds to complete.'.format(name=func.__name__, time=result_time))
# 	return wrapper