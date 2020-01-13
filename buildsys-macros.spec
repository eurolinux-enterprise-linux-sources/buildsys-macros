%global __version el8
 
Name:       buildsys-macros-%{__version}
Summary:    Macros for Koji BuildDystem
Version:    1.0
Release:    0%{?dist}
License:    GPL
Group:      Development/Buildsystem
BuildArch:  noarch
 
%description
This package contains macros for EuroLinux Build.
 
%prep
 
%build
 
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/etc/rpm/
echo -n -e  '%rhel 8\n' > %{buildroot}/etc/rpm/macros.disttag
# Some packages support CentOS
echo -n -e  '%centos 8\n' >> %{buildroot}/etc/rpm/macros.disttag
echo -n -e  '%eurolinux 8\n' >> %{buildroot}/etc/rpm/macros.disttag
echo -n -e  '%dist .%{__version}\n' >> %{buildroot}/etc/rpm/macros.disttag
echo -n -e  '%el8 1\n' >> %{buildroot}/etc/rpm/macros.disttag
echo -n -e "%__arch_install_post /usr/lib/rpm/check-buildroot\n" > %{buildroot}/etc/rpm/macros.checkbuild
 
%clean
rm -rf %{buildroot}
 
%files
%defattr(-,root,root)
/etc/rpm/macros.disttag
/etc/rpm/macros.checkbuild
 
%changelog
* Mon Jan 13 2020 Aleksander Baranowski <ab@euro-linux.com> - 1.0.0.el8
- Initial release
