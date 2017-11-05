
#returns value, start_index, end_index
def max_subseq(value_list,):
	
	l = len(value_list)
	if l == 0:
		raise error
	if l == 1:
		return [value_list[0], 0, 0, 0, value_list[0]]
	
	else:

		curr_val = value_list[l-1]
		del	value_list[l-1]
		
		pre_values = max_subseq(value_list)
		new_max = pre_values[0] + curr_val
		'''
		print ('++++++++++++++++'')
		print ('pre_max, pre_start, pre_end , pre_index , max_sum', pre_values)
		print ('curr_val', curr_val)
		print ('new_max',new_max)
		print ('++++++++++++++++'')
		'''
		pre_index = pre_values[3]
		max_sum = pre_values[4]
		start_index = pre_values[1]
		end_index = pre_values[2]
		
		if (new_max >= curr_val):
			if ((new_max > max_sum) or ((new_max == max_sum) and (end-start <= (pre_index-l-1)))):
				max_sum = new_max
				end_index = l-1
				start_index = pre_index
				
			return [new_max, start_index, end_index, pre_index, max_sum]
		else:
			pre_index = l-1
			if ((curr_val > max_sum) or ((curr_val == max_sum) and (end == start))):
				max_sum = curr_val
				start_index = pre_index
				end_index = start_index
			return [curr_val, start_index, end_index, pre_index, max_sum]
			




values = max_subseq([1,-2,4,5,-2,9,-2])

print ('sum is: ', values[4])
print ('start index is: ', values[1])
print ('end index is: ', values[2])


