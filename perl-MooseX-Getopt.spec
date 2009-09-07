%define upstream_name    MooseX-Getopt
%define upstream_version 0.22

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

License:    GPL+ or Artistic
Group:      Development/Perl
Summary:    Optional meta attribute trait for ignoring params
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl-devel
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(Getopt::Long::Descriptive)
BuildRequires: perl(IO::Scalar)
BuildRequires: perl(Moose)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}
BuildArch: noarch

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc ChangeLog README
%{_mandir}/man3/*
%perl_vendorlib/*


