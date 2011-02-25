#
# Conditional build:
%bcond_with	tests	# do not perform "make test" (disabled since uses network)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Tie
%define		pnam	TinyURL
Summary:	Tie::TinyURL Perl module - Tied interface to TinyURLURL.com
Name:		perl-Tie-TinyURL
Version:	0.02
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/N/NI/NICOLAW/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7419627ca7a8fe75e1fe1ca7dc81174a
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Tie::TinyURL module provides a very basic tied interface to the
TinyURLURL.com web service.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
echo n | %{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Tie/TinyURL.pm
%{_mandir}/man3/*
