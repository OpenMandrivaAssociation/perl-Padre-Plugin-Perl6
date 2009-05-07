
%define realname   Padre-Plugin-Perl6
%define version    0.37
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Perl document syntax-checking in the background
Source:     http://www.cpan.org/modules/by-module/Padre/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
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

%description
This class implements syntax checking of Perl documents in the background.
It inherits from the Padre::Task::SyntaxChecker manpage. Please read its
documentation!

%prep
%setup -q -n %{realname}-%{version} 

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


