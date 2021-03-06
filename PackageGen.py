import os
import zipfile
import zlib

def make_rel_archive(a_parent, a_name):
	archive = zipfile.ZipFile("build/" + a_name + ".zip", "w", zipfile.ZIP_DEFLATED)
	def do_write(a_relative):
		archive.write(a_parent + a_relative, a_relative)

	do_write("SKSE/Plugins/" + a_name + ".dll")
	do_write("SKSE/Plugins/" + a_name + ".json")

def make_dbg_archive(a_parent, a_name):
	archive = zipfile.ZipFile("build/" + a_name + "_pdb" + ".zip", "w", zipfile.ZIP_DEFLATED)
	archive.write(a_parent + "SKSE/Plugins/" + a_name + ".pdb", a_name + ".pdb")

def main():
	os.chdir(os.path.dirname(os.path.realpath(__file__)))
	try:
		os.mkdir("build")
	except FileExistsError:
		pass

	parent = os.environ["Skyrim64Path"] + "/Data/"
	for file in os.listdir("."):
		if file.endswith(".sln"):
			proj = file.removesuffix(".sln")
			make_rel_archive(parent, proj)
			make_dbg_archive(parent, proj)
			break
	
if __name__ == "__main__":
	main()
