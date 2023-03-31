%define module psycopg2

Summary:	PostgreSQL database adapter for Python
Name:		python-%{module}
Version:	2.9.3
Release:	3
Group:		Development/Python
License:	GPLv2 and ZPLv2.1 and BSD
Url:		http://www.psycopg.org/psycopg/
Source0:	https://files.pythonhosted.org/packages/fd/ae/98cb7a0cbb1d748ee547b058b14604bd0e9bf285a8e0cc5d148f8a8a952e/psycopg2-%{version}.tar.gz
BuildRequires:	postgresql-devel
BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(setuptools)

%description
psycopg is a PostgreSQL database adapter for the Python programming
language (just like pygresql and popy.) It was written from scratch with
the aim of being very small and fast, and stable as a rock. The main
advantages of psycopg are that it supports the full Python DBAPI-2.0 and
being thread safe at level 2.

psycopg2 is an almost complete rewrite of the psycopg 1.1.x branch.

%prep
%setup -qn %{module}-%{version}

%build
export CFLAGS="%{optflags}"
%{__python} setup.py build

%install
%{__python} setup.py install --root=%{buildroot}

%files
%doc AUTHORS NEWS  LICENSE  README.rst
%{python_sitearch}/psycopg2-%{version}-py*.*.egg-info
%{python_sitearch}/psycopg2/
