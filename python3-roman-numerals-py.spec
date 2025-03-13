# Conditional build:
%bcond_without	tests	# unit tests

%define		module	roman-numerals-py
Summary:	A library for manipulating well-formed Roman numerals
Name:		python3-%{module}
Version:	3.1.0
Release:	2
License:	CC0 1.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/MODULE/
Source0:	https://files.pythonhosted.org/packages/source/r/roman_numerals_py/roman_numerals_py-%{version}.tar.gz
# Source0-md5:	818e8252ca189c657bf7f860824eceb9
URL:		https://pypi.org/project/roman-numerals-py/
BuildRequires:	python3-build
BuildRequires:	python3-flit_core
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.2
%if %{with tests}
BuildRequires:	python3-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library for manipulating well-formed Roman numerals.

Integers between 1 and 3,999 (inclusive) are supported. Numbers beyond
this range will return an OutOfRangeError.

The classical system of roman numerals requires that the same
character may not appear more than thrice consecutively, meaning that
‘MMMCMXCIX' (3,999) is the largest well-formed Roman numeral. The
smallest is ‘I' (1), as there is no symbol for zero in Roman numerals.

Both upper- and lower-case formatting of roman numerals are supported,
and likewise for parsing strings, although the entire string must be
of the same case. Numerals that do not adhere to the classical form
are rejected with an InvalidRomanNumeralError.

%prep
%setup -q -n roman_numerals_py-%{version}

%build
%py3_build_pyproject

%if %{with tests}
# use explicit plugins list for reliable builds (delete PYTEST_PLUGINS if empty)
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS= \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENCE.rst README.rst
%{py3_sitescriptdir}/roman_numerals
%{py3_sitescriptdir}/roman_numerals_py-%{version}.dist-info
