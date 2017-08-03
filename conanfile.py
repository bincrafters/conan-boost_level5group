from conans import ConanFile, tools, os


class BoostLevel5GroupConan(ConanFile):
    name = "Boost.Level5Group"
    version = "1.64.0"
    generators = "txt"
    url = "https://github.com/bincrafters/conan-boost-level5group"
    description = "Special package with all members of cyclic dependency group"
    license = "www.boost.org/users/license.html"
    requires = "Boost.Assert/1.64.0@bincrafters/testing", \
        "Boost.Bind/1.64.0@bincrafters/testing", \
        "Boost.Config/1.64.0@bincrafters/testing", \
        "Boost.Core/1.64.0@bincrafters/testing", \
        "Boost.Move/1.64.0@bincrafters/testing", \
        "Boost.Predef/1.64.0@bincrafters/testing", \
        "Boost.Preprocessor/1.64.0@bincrafters/testing", \
        "Boost.Smart_Ptr/1.64.0@bincrafters/testing", \
        "Boost.Static_Assert/1.64.0@bincrafters/testing", \
        "Boost.Throw_Exception/1.64.0@bincrafters/testing",\
        "Boost.Type_Traits/1.64.0@bincrafters/testing"

    # Concept_Check Dependencies
    # config0 core2 mpl5 preprocessor0 type_traits3

    # Conversion Dependencies
    # assert1 config0 smart_ptr4 throw_exception2 type_traits3 typeof5

    # Detail Dependencies
    # config0 core2 mpl5 preprocessor0 static_assert1 type_traits3

    # Function Dependencies
    # assert1 bind3 config0 core2 integer3 move3 mpl5 preprocessor0 throw_exception2 type_index5 type_traits3 typeof5

    # Function_Types Dependencies
    # config0 core2 detail5 mpl5 preprocessor0 type_traits3

    # Functional Dependencies
    # assert1 config0 core2 detail5 function5 function_types5 integer3 iterator5 mpl5 optional5
    # preprocessor0 static_assert1 type_traits3 typeof5 utility5

    # Fusion Dependencies
    # config0 core2 function_types5 functional5 mpl5 preprocessor0 static_assert1 tuple4 type_traits3 typeof5 utility5

    # Iterator Dependencies
    # assert1 concept_check5 config0 conversion5 core2 detail5 function_types5 fusion5 mpl5
    # optional5 smart_ptr4 static_assert1 type_traits3 utility5

    # Mpl Dependencies
    # config0 core2 predef0 preprocessor0 static_assert1 type_traits3 utility5

    # Optional Dependencies
    # assert1 config0 core2 detail5 move3 mpl5 static_assert1 throw_exception2 type_traits3 utility5

    # Type_Index Dependencies
    # config0 core2 functional5 mpl5 preprocessor0 smart_ptr4 static_assert1 throw_exception2 type_traits3

    # Typeof Dependencies
    # config0 core2 mpl5 preprocessor0 type_traits3

    # Utility Dependencies
    # config0 core2 iterator5 mpl5 preprocessor0 static_assert1 throw_exception2 type_traits3

    def source(self):
        self.run("git clone --depth=50 --branch=boost-{0} {1}.git"
                 .format(self.version, "https://github.com/boostorg/concept_check"))     

        self.run("git clone --depth=50 --branch=boost-{0} {1}.git"
                 .format(self.version, "https://github.com/boostorg/conversion"))

        self.run("git clone --depth=50 --branch=boost-{0} {1}.git"
                 .format(self.version, "https://github.com/boostorg/detail"))

        self.run("git clone --depth=50 --branch=boost-{0} {1}.git"
                 .format(self.version, "https://github.com/boostorg/function"))

        self.run("git clone --depth=50 --branch=boost-{0} {1}.git"
                 .format(self.version, "https://github.com/boostorg/function_types"))

        self.run("git clone --depth=50 --branch=boost-{0} {1}.git"
                 .format(self.version, "https://github.com/boostorg/functional"))

        self.run("git clone --depth=50 --branch=boost-{0} {1}.git"
                 .format(self.version, "https://github.com/boostorg/fusion"))
                 
        self.run("git clone --depth=50 --branch=boost-{0} {1}.git"
                 .format(self.version, "https://github.com/boostorg/iterator"))
                        
        self.run("git clone --depth=50 --branch=boost-{0} {1}.git"
                 .format(self.version, "https://github.com/boostorg/mpl"))     

        self.run("git clone --depth=50 --branch=boost-{0} {1}.git"
                 .format(self.version, "https://github.com/boostorg/optional"))

        self.run("git clone --depth=50 --branch=boost-{0} {1}.git"
                 .format(self.version, "https://github.com/boostorg/type_index"))

        self.run("git clone --depth=50 --branch=boost-{0} {1}.git"
                 .format(self.version, "https://github.com/boostorg/typeof"))
                 
        self.run("git clone --depth=50 --branch=boost-{0} {1}.git"
                 .format(self.version, "https://github.com/boostorg/utility"))
                 
    def package(self):

        concept_check_dir = os.path.join(self.build_folder, "concept_check", "include")
        self.copy(pattern="*", dst="include", src=concept_check_dir)

        conversion_dir = os.path.join(self.build_folder, "conversion", "include")
        self.copy(pattern="*", dst="include", src=conversion_dir)
        
        detail_dir = os.path.join(self.build_folder, "detail", "include")
        self.copy(pattern="*", dst="include", src=detail_dir)

        function_dir = os.path.join(self.build_folder, "function", "include")
        self.copy(pattern="*", dst="include", src=function_dir)

        function_types_dir = os.path.join(self.build_folder, "function_types", "include")
        self.copy(pattern="*", dst="include", src=function_types_dir)

        functional_dir = os.path.join(self.build_folder, "functional", "include")
        self.copy(pattern="*", dst="include", src=functional_dir)

        fusion_dir = os.path.join(self.build_folder, "fusion", "include")
        self.copy(pattern="*", dst="include", src=fusion_dir)

        iterator_dir = os.path.join(self.build_folder, "iterator", "include")
        self.copy(pattern="*", dst="include", src=iterator_dir)
        
        mpl_dir = os.path.join(self.build_folder, "mpl", "include")
        self.copy(pattern="*", dst="include", src=mpl_dir)
        
        optional_dir = os.path.join(self.build_folder, "optional", "include")
        self.copy(pattern="*", dst="include", src=optional_dir)

        functional_dir = os.path.join(self.build_folder, "type_index", "include")
        self.copy(pattern="*", dst="include", src=functional_dir)

        functional_dir = os.path.join(self.build_folder, "typeof", "include")
        self.copy(pattern="*", dst="include", src=functional_dir)

        utility_dir = os.path.join(self.build_folder, "utility", "include")
        self.copy(pattern="*", dst="include", src=utility_dir)
        
    def package_id(self):
        self.info.header_only()
