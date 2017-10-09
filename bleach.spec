#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : bleach
Version  : 2.1.1
Release  : 8
URL      : http://pypi.debian.net/bleach/bleach-2.1.1.tar.gz
Source0  : http://pypi.debian.net/bleach/bleach-2.1.1.tar.gz
Summary  : An easy safelist-based HTML-sanitizing tool.
Group    : Development/Tools
License  : Apache-2.0
Requires: bleach-legacypython
Requires: bleach-python3
Requires: bleach-python
Requires: Sphinx
Requires: flake8
Requires: html5lib
Requires: pytest
Requires: six
Requires: tox
BuildRequires : html5lib
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv

%description
Bleach
        ======

%package legacypython
Summary: legacypython components for the bleach package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the bleach package.


%package python
Summary: python components for the bleach package.
Group: Default
Requires: bleach-legacypython
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
%setup -q -n bleach-2.1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507573560
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1507573560
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
