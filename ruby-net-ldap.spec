%define tarname net-ldap
Summary:	LDAP module for Ruby
Summary(pl.UTF-8):	Moduł LDAP dla języka Ruby
Name:		ruby-net-ldap
Version:	0.0.4
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/12430/%{name}-%{version}.tar.gz
# Source0-md5:	99822b93260f88bd85f357a004d687a2
URL:		http://rubyforge.org/projects/net-ldap/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
BuildRequires:	setup.rb = 3.3.1
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LDAP module for Ruby.

%description -l pl.UTF-8
Moduł LDAP dla języka Ruby.

%prep
%setup -q
cp %{_datadir}/setup.rb .

%build
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}
ruby setup.rb setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_archdir}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%{ruby_rubylibdir}/net/*
