#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : bleach
Version  : 4.1.0
Release  : 53
URL      : https://files.pythonhosted.org/packages/6a/a3/217842324374fd3fb33db0eb4c2909ccf3ecc5a94f458088ac68581f8314/bleach-4.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/6a/a3/217842324374fd3fb33db0eb4c2909ccf3ecc5a94f458088ac68581f8314/bleach-4.1.0.tar.gz
Summary  : An easy safelist-based HTML-sanitizing tool.
Group    : Development/Tools
License  : Apache-2.0
Requires: bleach-license = %{version}-%{release}
Requires: bleach-python = %{version}-%{release}
Requires: bleach-python3 = %{version}-%{release}
Requires: packaging
Requires: six
Requires: webencodings
BuildRequires : buildreq-distutils3
BuildRequires : html5lib
BuildRequires : packaging
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv
BuildRequires : webencodings

%description
Bleach
        ======

%package license
Summary: license components for the bleach package.
Group: Default

%description license
license components for the bleach package.


%package python
Summary: python components for the bleach package.
Group: Default
Requires: bleach-python3 = %{version}-%{release}

%description python
python components for the bleach package.


%package python3
Summary: python3 components for the bleach package.
Group: Default
Requires: python3-core
Provides: pypi(bleach)
Requires: pypi(packaging)
Requires: pypi(six)
Requires: pypi(webencodings)

%description python3
python3 components for the bleach package.


%prep
%setup -q -n bleach-4.1.0
cd %{_builddir}/bleach-4.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635707168
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/bleach
cp %{_builddir}/bleach-4.1.0/LICENSE %{buildroot}/usr/share/package-licenses/bleach/2712eb1e3c7cc1e80a68d7eea6acb5299222f242
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/bleach/2712eb1e3c7cc1e80a68d7eea6acb5299222f242

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
