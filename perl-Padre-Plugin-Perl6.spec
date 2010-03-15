%define upstream_name    Padre-Plugin-Perl6
%define upstream_version 0.63

# find-requires extracts too much, cf https://qa.mandriva.com/show_bug.cgi?id=47678
# therefore, forcing explicit require skipping of Win32
%define _requires_exceptions perl.Win32.

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

License:    GPL+ or Artistic
Group:      Development/Perl
Summary:    Perl document syntax-checking in the background
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Padre/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(App::Grok)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(IPC::Run3)
BuildRequires: perl(Padre)
BuildRequires: perl(Readonly)
BuildRequires: perl(Syntax::Highlight::Perl6)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::NeedsDisplay)
BuildRequires: perl(Test::NoWarnings)
BuildRequires: perl(URI)

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This class implements syntax checking of Perl documents in the background.
It inherits from the Padre::Task::SyntaxChecker manpage. Please read its
documentation!

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
#make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes
%{_mandir}/man3/*
%perl_vendorlib/*
