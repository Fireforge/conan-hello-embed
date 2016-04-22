import os
from conans import ConanFile, CMake
   
class HelloConan(ConanFile):
   name = "Hello"
   version = "0.1"
   license="MIT"
   settings = "os", "compiler", "build_type", "arch"
   url = "https://github.com/memsharded/conan-hello-embed.git"
   exports = "CMakeLists.txt", "hello.*", "main.cpp", "LICENSE", "README.md"

   def build(self):
       os.mkdir('build')
       os.chdir('build')
       
       self.run('conan install ..')
       
       cmake = CMake(self.settings)
       self.run('cmake ..\\src %s' % cmake.command_line)
       self.run("cmake --build . %s" % cmake.build_config)

   def package(self):
       self.copy("*.h", dst="include")
       self.copy("*.lib", dst="lib", src="lib")
       self.copy("*.a", dst="lib", src="lib")

   def package_info(self):
       self.cpp_info.libs = ["hello"]
