from conans import ConanFile, CMake


class StringPrinterConan(ConanFile):
    name = "stringprinter"
    #version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports_sources = "*"
    requires = "stringprovider/[>=1.0 <2.1]@me/dev"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="src")
        self.copy("*.lib", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["stringprinter"]
