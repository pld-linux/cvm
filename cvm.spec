# TODO:
# - separate -devel package
# - think how to fix --as-needed this time
Summary:	Credential Validation Modules
Summary(pl.UTF-8):	Moduły uwierzytelniające CVM
Name:		cvm
Version:	0.82
Release:	0.1
License:	GPL
Group:		Development/Libraries
Source0:	http://untroubled.org/cvm/%{name}-%{version}.tar.gz
# Source0-md5:	c8ce29c3b0ec932ae2d8c0c0eb94915a
URL:		http://untroubled.org/cvm/
BuildRequires:	bglibs-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         filterout_ld    -Wl,--as-needed

%description
This package implements the CVM interface as a client
(cvm-testclient), and as a module (cvm-unix, cvm-pwfile).

%description -l pl.UTF-8
Pakiet implementuje interfejs CVM od strony klienta (cvm-testclient) i
modułów (cvm-unix, cvm-pwfile).

%prep
%setup -q

%build
echo '%{__cc} %{rpmcflags} -Wall -I%{_includedir}/bglibs' > conf-cc
echo '%{__cc} %{rpmldflags} -L%{_libdir}/bglibs' > conf-ld
echo '%{_includedir}/bglibs' > conf-bgincs
echo '%{_libdir}/bglibs' > conf-bglibs
echo '%{_prefix}' > conf-home
echo '%{_bindir}' > conf-bin
echo '%{_includedir}' > conf-include
echo '%{_libdir}' > conf-lib

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	install_prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
# FIXME: errogenous!
%{_libdir}/*
%{_includedir}/*
