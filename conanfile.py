from conans import ConanFile, tools


class BoostLevel5GroupConan(ConanFile):
    name = "Boost.Level5Group"
    version = "1.65.1"
    url = "https://github.com/bincrafters/conan-boost-level5group"
    description = "Special package with all members of cyclic dependency group"
    license = "www.boost.org/users/license.html"

    requires = \
        "Boost.Assert/1.65.1@bincrafters/testing", \
        "Boost.Bind/1.65.1@bincrafters/testing", \
        "Boost.Config/1.65.1@bincrafters/testing", \
        "Boost.Core/1.65.1@bincrafters/testing", \
        "Boost.Move/1.65.1@bincrafters/testing", \
        "Boost.Predef/1.65.1@bincrafters/testing", \
        "Boost.Preprocessor/1.65.1@bincrafters/testing", \
        "Boost.Smart_Ptr/1.65.1@bincrafters/testing", \
        "Boost.Static_Assert/1.65.1@bincrafters/testing", \
        "Boost.Throw_Exception/1.65.1@bincrafters/testing", \
        "Boost.Type_Traits/1.65.1@bincrafters/testing"

    lib_short_names = [
        "concept_check", "conversion", "detail", "function", "function_types",
        "functional", "fusion", "iterator", "mpl", "optional", "type_index",
        "typeof", "utility"]
    is_header_only = True
    is_cycle_group = True

    # BEGIN

    short_paths = True
    build_requires = "Boost.Generator/1.65.1@bincrafters/testing"

    def package_id(self):
        self.info.header_only()

    @property
    def env(self):
        try:
            with tools.pythonpath(super(self.__class__, self)):
                import boostgenerator # pylint: disable=F0401
                boostgenerator.BoostConanFile(self)
        except:
            pass
        return super(self.__class__, self).env

    # END
