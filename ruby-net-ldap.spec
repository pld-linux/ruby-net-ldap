%define pkgname net-ldap
Summary:	LDAP module for Ruby
Summary(pl.UTF-8):	Moduł LDAP dla języka Ruby
Name:		ruby-%{pkgname}
Version:	0.1.1
Release:	2
License:	GPL
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	9df57177e5f51fc5e15956371d57e307
URL:		http://rubyforge.org/projects/net-ldap/
BuildRequires:	rpmbuild(macros) >= 1.484
BuildRequires:	ruby >= 1:1.9
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LDAP module for Ruby.

%description -l pl.UTF-8
Moduł LDAP dla języka Ruby.

%package rdoc
Summary:	HTML documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie HTML dla %{pkgname}
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
HTML documentation for %{pkgname}.

%description rdoc -l pl.UTF-8
Dokumentacja w formacie HTML dla %{pkgname}.

%package ri
Summary:	ri documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie ri dla %{pkgname}
Group:		Documentation
Requires:	ruby

%description ri
ri documentation for %{pkgname}.

%description ri -l pl.UTF-8
Dokumentacji w formacie ri dla %{pkgname}.

%prep
%setup -q -c
%{__tar} xf %{SOURCE0} -O data.tar.gz | %{__tar} xz
find -newer README.txt -o -print | xargs touch --reference %{SOURCE0}

%build
rdoc --ri --op ri lib
rdoc --op rdoc lib
rm -r ri/{Array,Bignum,FalseClass,Fixnum,IO,OpenSSL,String,StringIO,TrueClass} \
	ri/Net/{SNMP,SnmpPdu}
rm ri/created.rid

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir},%{ruby_rdocdir}}

cp -a lib/* $RPM_BUILD_ROOT%{ruby_rubylibdir}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%{ruby_rubylibdir}/net-ldap.rb
%{ruby_rubylibdir}/net/*

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}

%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/Net/BER
%{ruby_ridir}/Net/LDAP
%{ruby_ridir}/Net/LDIF
%{ruby_ridir}/Net/LdapPdu
%{ruby_ridir}/Net/LdapPduError
