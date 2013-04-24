%define pkgname net-ldap
Summary:	LDAP module for Ruby
Summary(pl.UTF-8):	Moduł LDAP dla języka Ruby
Name:		ruby-%{pkgname}
Version:	0.3.1
Release:	2
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	96c39c91619446256936b3c81b554c93
URL:		http://rubygems.org/gems/net-ldap
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildRequires:	ruby >= 1:1.8.7
BuildArch:	noarch
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
%setup -q -n %{pkgname}-%{version}

%build
rdoc --ri --op ri lib
rdoc --op rdoc lib
rm -r ri/{Array,Bignum,FalseClass,Fixnum,IO,OpenSSL,String,StringIO,TrueClass,Net/cdesc-Net.ri}
rm ri/created.rid
rm ri/cache.ri

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_ridir},%{ruby_rdocdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rdoc License.rdoc History.rdoc Hacking.rdoc Contributors.rdoc
%{ruby_vendorlibdir}/net-ldap.rb
%{ruby_vendorlibdir}/net/ber.rb
%{ruby_vendorlibdir}/net/ldap.rb
%{ruby_vendorlibdir}/net/snmp.rb
%{ruby_vendorlibdir}/net/ber
%{ruby_vendorlibdir}/net/ldap

# TODO: package in ruby base dirs?
%dir %{ruby_vendorlibdir}/net

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}

%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/Net/BER
%{ruby_ridir}/Net/LDAP
# yes, it packages some snmp libs to
%{ruby_ridir}/SNMP
%{ruby_ridir}/SnmpPdu
