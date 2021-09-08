import os
from conans import ConanFile, tools


class ProjectTestConan(ConanFile):

    def imports(self):
        self.copy("*.exe", dst="bin", src="bin")

    def test(self):
        if not tools.cross_building(self):
            os.chdir("bin")
            self.run(f".{os.sep}project")
