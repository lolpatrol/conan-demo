from conans import ConanFile, CMake


class ApplicationConan(ConanFile):
    name = "application"
    version = "1.0"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports_sources = "*"
    requires = "stringprinter/1.0@me/dev"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*.exe", dst="bin", src="bin")

