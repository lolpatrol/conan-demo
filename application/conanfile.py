from conans import ConanFile, CMake


class ApplicationConan(ConanFile):
    name = "application"
    # version = "0.1.0"
    settings = "os", "compiler", "build_type", "arch"

    requires = "stringprinter/0.1.0@lolpatrol/dev"
    generators = "cmake"

    exports_sources = "*"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*.exe", dst="bin", src="bin")

