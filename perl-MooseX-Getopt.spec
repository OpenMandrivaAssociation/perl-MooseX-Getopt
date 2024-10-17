%define upstream_name    MooseX-Getopt
%define upstream_version 0.47

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Optional meta attribute trait for ignoring params
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Getopt::Long)
BuildRequires:	perl(Getopt::Long::Descriptive)
BuildRequires:	perl(IO::Scalar)
BuildRequires:	perl(Moose)
BuildRequires:	perl(MooseX::Role::Parameterized)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Requires)
BuildRequires:	perl(Test::Trap)
BuildRequires:	perl(Test::Warn)
BuildRequires:	perl-devel
BuildArch:	noarch

Requires:	perl(Getopt::Long::Descriptive)

%description
This is a role which provides an alternate constructor for creating objects
using parameters passed in from the command line.

This module attempts to DWIM as much as possible with the command line
params by introspecting your class's attributes. It will use the name of
your attribute as the command line option, and if there is a type
constraint defined, it will configure Getopt::Long to handle the option
accordingly.

You can use the trait the MooseX::Getopt::Meta::Attribute::Trait manpage or
the attribute metaclass the MooseX::Getopt::Meta::Attribute manpage to get
non-default commandline option names and aliases.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*


%changelog
* Mon Apr 18 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.370.0-1mdv2011.0
+ Revision: 655773
- update to new version 0.37
- update to new version 0.36

* Sun Feb 13 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.350.0-1
+ Revision: 637622
- update to new version 0.35

* Sat Aug 28 2010 Jérôme Quelin <jquelin@mandriva.org> 0.330.0-1mdv2011.0
+ Revision: 573856
- adding missing buildrequires:
- update to 0.33

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.310.0-1mdv2011.0
+ Revision: 552416
- update to 0.31

* Tue Mar 02 2010 Jérôme Quelin <jquelin@mandriva.org> 0.270.0-1mdv2010.1
+ Revision: 513476
- update to 0.27

* Sat Dec 12 2009 Jérôme Quelin <jquelin@mandriva.org> 0.260.0-1mdv2010.1
+ Revision: 477621
- update to 0.26

* Sun Nov 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.250.0-1mdv2010.1
+ Revision: 471065
- update to 0.25

* Tue Nov 17 2009 Jérôme Quelin <jquelin@mandriva.org> 0.240.0-2mdv2010.1
+ Revision: 466990
- adding requires: not found by rpm

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.240.0-1mdv2010.1
+ Revision: 461764
- update to 0.24
- update to 0.06
- update to 0.06

* Mon Sep 07 2009 Jérôme Quelin <jquelin@mandriva.org> 0.220.0-1mdv2010.0
+ Revision: 432324
- update to 0.22

* Fri Aug 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.210.0-1mdv2010.0
+ Revision: 421836
- update to 0.21

* Sun Jul 12 2009 Jérôme Quelin <jquelin@mandriva.org> 0.200.0-1mdv2010.0
+ Revision: 394972
- update to 0.20

* Thu Jul 09 2009 Jérôme Quelin <jquelin@mandriva.org> 0.190.0-1mdv2010.0
+ Revision: 393832
- adding missing buildrequires:
- using %%perl_convert_version
- fixed license field

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - update to new version 0.19

* Sat May 02 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.18-1mdv2010.0
+ Revision: 370495
- update to new version 0.18

* Sun Mar 08 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.16-1mdv2009.1
+ Revision: 352914
- update to new version 0.16

* Wed Dec 03 2008 Jérôme Quelin <jquelin@mandriva.org> 0.15-1mdv2009.1
+ Revision: 309768
- import perl-MooseX-Getopt


* Wed Dec 03 2008 cpan2dist 0.15-1mdv
- initial mdv release, generated with cpan2dist

