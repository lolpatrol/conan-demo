from conans import ConanFile, CMake


class ProjectConan(ConanFile):
    name = "project"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports_sources = "*"
    requires = "sayhi/1.0@me/dev"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*.exe", dst="bin", src="bin")

