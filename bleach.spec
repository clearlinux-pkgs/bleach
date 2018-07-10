#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : bleach
Version  : 1.5.0
Release  : 24
URL      : http://pypi.debian.net/bleach/bleach-1.5.0.tar.gz
Source0  : http://pypi.debian.net/bleach/bleach-1.5.0.tar.gz
Summary  : An easy whitelist-based HTML-sanitizing tool.
Group    : Development/Tools
License  : Apache-2.0
Requires: bleach-python3
Requires: bleach-license
Requires: bleach-python
Requires: html5lib
Requires: six
BuildRequires : html5lib
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv

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
Requires: bleach-python3

%description python
python components for the bleach package.


%package python3
Summary: python3 components for the bleach package.
Group: Default
Requires: python3-core

%description python3
python3 components for the bleach package.


%prep
%setup -q -n bleach-1.5.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1529093276
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/bleach
cp LICENSE %{buildroot}/usr/share/doc/bleach/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/bleach/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
