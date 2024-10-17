%define upstream_name    Padre-Plugin-Perl6
%define upstream_version 0.71

# find-requires extracts too much, cf https://qa.mandriva.com/show_bug.cgi?id=47678
# therefore, forcing explicit require skipping of Win32
%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Win32(.*)\\)'
%else
%define _requires_exceptions perl.Win32.
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

License:	GPL+ or Artistic
Group:		Development/Perl
Summary:	Perl document syntax-checking in the background
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Padre/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(App::Grok)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::ShareDir::Install)
BuildRequires:	perl(IPC::Run3)
BuildRequires:	perl(Padre)
BuildRequires: 	perl(Perl6::Refactor)
BuildRequires:	perl(Readonly)
BuildRequires:	perl(Syntax::Highlight::Perl6)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::NeedsDisplay)
BuildRequires:	perl(Test::NoWarnings)
BuildRequires:	perl(URI)

BuildArch:	noarch

%description
This class implements syntax checking of Perl documents in the background.
It inherits from the Padre::Task::SyntaxChecker manpage. Please read its
documentation!

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
#make test

%install
%makeinstall_std

%files
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.710.0-2mdv2011.0
+ Revision: 656955
- rebuild for updated spec-helper

* Sun Dec 19 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.710.0-1mdv2011.0
+ Revision: 622928
- update to new version 0.71

* Sun May 09 2010 Jérôme Quelin <jquelin@mandriva.org> 0.640.0-1mdv2011.0
+ Revision: 544154
- update to 0.64

* Mon Mar 15 2010 Jérôme Quelin <jquelin@mandriva.org> 0.630.0-1mdv2010.1
+ Revision: 520129
- update to 0.63

* Thu Jan 07 2010 Jérôme Quelin <jquelin@mandriva.org> 0.620.0-1mdv2010.1
+ Revision: 487197
- update to 0.62

* Sat Dec 12 2009 Jérôme Quelin <jquelin@mandriva.org> 0.610.0-1mdv2010.1
+ Revision: 477629
- update to 0.61

* Sat Sep 19 2009 Jérôme Quelin <jquelin@mandriva.org> 0.600.0-1mdv2010.0
+ Revision: 444608
- update to 0.60

* Wed Sep 09 2009 Jérôme Quelin <jquelin@mandriva.org> 0.590.0-1mdv2010.0
+ Revision: 435707
- update to 0.59

* Tue Aug 25 2009 Jérôme Quelin <jquelin@mandriva.org> 0.580.0-1mdv2010.0
+ Revision: 420891
- update to 0.58

* Wed Aug 19 2009 Jérôme Quelin <jquelin@mandriva.org> 0.570.0-1mdv2010.0
+ Revision: 418121
- update to 0.57

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.560.0-1mdv2010.0
+ Revision: 402141
- update to 0.56

* Sat Jul 25 2009 Jérôme Quelin <jquelin@mandriva.org> 0.540.0-1mdv2010.0
+ Revision: 399597
- update to 0.54

* Thu Jul 23 2009 Jérôme Quelin <jquelin@mandriva.org> 0.530.0-1mdv2010.0
+ Revision: 398911
- update to 0.53

* Sat Jul 11 2009 Jérôme Quelin <jquelin@mandriva.org> 0.500.0-1mdv2010.0
+ Revision: 394712
- update to 0.50

* Sun May 31 2009 Jérôme Quelin <jquelin@mandriva.org> 0.410.0-1mdv2010.0
+ Revision: 381589
- update to 0.41
- using %%perl_convert_version
- fix license field

* Sun May 24 2009 Jérôme Quelin <jquelin@mandriva.org> 0.40-1mdv2010.0
+ Revision: 379284
- update to new version 0.40

* Mon May 11 2009 Jérôme Quelin <jquelin@mandriva.org> 0.39-1mdv2010.0
+ Revision: 374151
- update to new version 0.39

* Thu May 07 2009 Jérôme Quelin <jquelin@mandriva.org> 0.37-2mdv2010.0
+ Revision: 372969
- removing automatic erroneous dependency

* Thu May 07 2009 Jérôme Quelin <jquelin@mandriva.org> 0.37-1mdv2010.0
+ Revision: 372850
- update to new version 0.37

* Wed May 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.36-1mdv2010.0
+ Revision: 372638
- updated to 0.36

* Tue Jan 13 2009 Jérôme Quelin <jquelin@mandriva.org> 0.025-1mdv2009.1
+ Revision: 329141
- import perl-Padre-Plugin-Perl6


* Tue Jan 13 2009 cpan2dist 0.025-1mdv
- initial mdv release, generated with cpan2dist

