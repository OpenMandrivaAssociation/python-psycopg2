%define module psycopg2

Summary:	PostgreSQL database adapter for Python
Name:		python-%{module}
Version:	2.9.3
Release:	1
Group:		Development/Python
License:	GPLv2 and ZPLv2.1 and BSD
Url:		http://www.psycopg.org/psycopg/
Source0:	https://files.pythonhosted.org/packages/fd/ae/98cb7a0cbb1d748ee547b058b14604bd0e9bf285a8e0cc5d148f8a8a952e/psycopg2-%{version}.tar.gz
BuildRequires:	postgresql-devel
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(python2)
BuildRequires:	python2dist(setuptools)
BuildRequires:	python3dist(setuptools)

%description
psycopg is a PostgreSQL database adapter for the Python programming
language (just like pygresql and popy.) It was written from scratch with
the aim of being very small and fast, and stable as a rock. The main
advantages of psycopg are that it supports the full Python DBAPI-2.0 and
being thread safe at level 2.

psycopg2 is an almost complete rewrite of the psycopg 1.1.x branch.

%package -n python2-%{module}
Summary:	PostgreSQL database adapter for Python
Group:	Development/Python

%description -n	python2-%{module}
PostgreSQL database adapter for Python

%prep
%setup -qn %{module}-%{version}

pushd ..
cp -Rp %{module}-%{version} %py2dir

%build
export CFLAGS="%{optflags}"
%{__python} setup.py build

pushd %py2dir
%{__python2} setup.py build

%install
%{__python} setup.py install --root=%{buildroot}

pushd %py2dir
%{__python2} setup.py install --root=%{buildroot}

%files
%doc AUTHORS NEWS  LICENSE  README.rst
%{py3_platsitedir}/psycopg2*


%files -n python2-%{module}
%doc AUTHORS NEWS  LICENSE  README.rst
%{py2_platsitedir}/psycopg2*
