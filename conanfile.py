#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools


class BoostLevel5GroupConan(ConanFile):
    name = "boost_level5group"
    version = "1.66.0"
    url = "https://github.com/bincrafters/conan-boost_level5group"
    author = "Bincrafters <bincrafters@gmail.com>"
    exports = ["LICENSE.md"]
    is_cycle_group = True
    is_header_only = True
    lib_short_names = [
        "concept_check", "conversion", "detail", "function", "function_types",
        "functional", "fusion", "iterator", "mpl", "optional", "type_index",
        "typeof", "utility"]


    def package_id_additional(self):
        self.info.header_only()

    requires = (
        "boost_package_tools/1.66.0@bincrafters/testing",
        "boost_assert/1.66.0@bincrafters/testing",
        "boost_bind/1.66.0@bincrafters/testing",
        "boost_config/1.66.0@bincrafters/testing",
        "boost_core/1.66.0@bincrafters/testing",
        "boost_integer/1.66.0@bincrafters/testing",
        "boost_move/1.66.0@bincrafters/testing",
        "boost_predef/1.66.0@bincrafters/testing",
        "boost_preprocessor/1.66.0@bincrafters/testing",
        "boost_smart_ptr/1.66.0@bincrafters/testing",
        "boost_static_assert/1.66.0@bincrafters/testing",
        "boost_throw_exception/1.66.0@bincrafters/testing",
        "boost_type_traits/1.66.0@bincrafters/testing"
    )

    # BEGIN

    description = "Please visit http://www.boost.org/doc/libs/1_66_0"
    license = "BSL-1.0"
    short_paths = True
    build_requires = "boost_generator/1.66.0@bincrafters/testing"

    def package_id(self):
        getattr(self, "package_id_additional", lambda:None)()

    def source(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.source(self)
        getattr(self, "source_additional", lambda:None)()

    def build(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.build(self)
        getattr(self, "build_additional", lambda:None)()

    def package(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.package(self)
        getattr(self, "package_additional", lambda:None)()

    def package_info(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.package_info(self)
        getattr(self, "package_info_additional", lambda:None)()



    # END
