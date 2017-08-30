from conans import ConanFile, tools, os


class BoostLevel5GroupConan(ConanFile):
    name = "Boost.Level5Group"
    version = "1.64.0"
    short_paths = True
    url = "https://github.com/bincrafters/conan-boost-level5group"
    description = "Special package with all members of cyclic dependency group"
    license = "www.boost.org/users/license.html"
    lib_short_names = ["concept_check", "conversion", "detail", "function", "function_types", "functional", "fusion", "iterator", "mpl", "optional", "type_index", "typeof", "utility"]
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
        boostorg_github = "https://github.com/boostorg"
        archive_name = "boost-" + self.version  
        for lib_short_name in self.lib_short_names:
            tools.get("{0}/{1}/archive/{2}.tar.gz"
                .format(boostorg_github, lib_short_name, archive_name))
            os.rename(lib_short_name + "-" + archive_name, lib_short_name)
                     
    def package(self):
        for lib_short_name in self.lib_short_names:
            include_dir = os.path.join(lib_short_name, "include")
            self.copy(pattern="*", dst="include", src=include_dir)
        
    def package_id(self):
        self.info.header_only()
