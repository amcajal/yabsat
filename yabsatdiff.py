import sys

########################################################################

def read_file (file_to_read):
	file_reader = open(file_to_read, 'r')
	content = file_reader.read().split("\n")
	content = filter(None, content)
	file_reader.close()
	return content


def textfile_to_map (file_to_read):
	the_map = {}
	content_as_list = read_file(file_to_read)
	for line in content_as_list:
		key, value = line.split(" ", 1)
		the_map[key] = value
	return the_map


def extract_unique_elements (list_one, list_two):
	unique_e = [x for x in list_one if x not in list_two]
	return unique_e


def extract_duplicate_elements (list_one, list_two):
	dupli_e = [x for x in list_one if x in list_two]
	return dupli_e


def extract_mod_files(dup_files, map_base_snapshot, map_new_state):
	mod_files_list = []
	for file in dup_files:
		old = map_base_snapshot[file]
		new = map_new_state[file]
		if (old != new):
			mod_files_list.append(file)
	return mod_files_list


def write_section(section_title, content, file_writer):
	file_writer.write(section_title)
	file_writer.write("="*20 + "\n")
	for entry in content:
		file_writer.write(entry)
		file_writer.write("\n")
	file_writer.write("\n\n")
	

def main(arg_list):
	map_base_snapshot = textfile_to_map(arg_list[1])
	map_new_state = textfile_to_map(arg_list[2])

	list_bs = list(map_base_snapshot) # bs stands for base_snapshot
	list_nw = list(map_new_state) # nw stants for new (state)

	deleted_files = extract_unique_elements(list_bs, list_nw)
	new_files = extract_unique_elements(list_nw, list_bs)
	dup_files = extract_duplicate_elements(list_bs, list_nw)
	
	mod_files = extract_mod_files(dup_files, map_base_snapshot, map_new_state)
	
	results_file = "./yabsatdiff_result.txt"
	file_writer = open(results_file, 'w')
	write_section("deleted files", deleted_files, file_writer)
	write_section("new files", new_files, file_writer)
	write_section("mod files", mod_files, file_writer)
	file_writer.close()
	return 0


def usage():
	print "Usage:"
	print "yabsatdiff.py <base_snapshot.txt> <new_state.txt>"

	
###############################################################################
if __name__ == "__main__":
	if (len(sys.argv) != 3):
		usage()
		sys.exit(1)

	main(sys.argv)
	sys.exit(0)




