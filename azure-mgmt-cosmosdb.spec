#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : azure-mgmt-cosmosdb
Version  : 6.0.0
Release  : 10
URL      : https://files.pythonhosted.org/packages/f8/95/42073501b8bd1271248cdb2592df7ad2842d81ef9baf2186758e5d1690f3/azure-mgmt-cosmosdb-6.0.0.zip
Source0  : https://files.pythonhosted.org/packages/f8/95/42073501b8bd1271248cdb2592df7ad2842d81ef9baf2186758e5d1690f3/azure-mgmt-cosmosdb-6.0.0.zip
Summary  : Microsoft Azure Cosmos DB Management Client Library for Python
Group    : Development/Tools
License  : MIT
Requires: azure-mgmt-cosmosdb-python = %{version}-%{release}
Requires: azure-mgmt-cosmosdb-python3 = %{version}-%{release}
Requires: azure-common~
Requires: azure-mgmt-core
Requires: azure-mgmt-nspkg
Requires: msrest
BuildRequires : azure-common~
BuildRequires : azure-mgmt-core
BuildRequires : azure-mgmt-nspkg
BuildRequires : buildreq-distutils3
BuildRequires : msrest

%description
This is the Microsoft Azure Cosmos DB Management Client Library.
        This package has been tested with Python 2.7, 3.5, 3.6, 3.7 and 3.8.

%package python
Summary: python components for the azure-mgmt-cosmosdb package.
Group: Default
Requires: azure-mgmt-cosmosdb-python3 = %{version}-%{release}

%description python
python components for the azure-mgmt-cosmosdb package.


%package python3
Summary: python3 components for the azure-mgmt-cosmosdb package.
Group: Default
Requires: python3-core
Provides: pypi(azure_mgmt_cosmosdb)
Requires: pypi(azure_common)
Requires: pypi(azure_mgmt_core)
Requires: pypi(msrest)

%description python3
python3 components for the azure-mgmt-cosmosdb package.


%prep
%setup -q -n azure-mgmt-cosmosdb-6.0.0
cd %{_builddir}/azure-mgmt-cosmosdb-6.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1608046151
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## Remove excluded files
rm -f %{buildroot}/usr/lib/python3*/site-packages/azure/mgmt/__init__.py
rm -f %{buildroot}/usr/lib/python3*/site-packages/azure/mgmt/__pycache__/__init__.cpython-3*.pyc

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
