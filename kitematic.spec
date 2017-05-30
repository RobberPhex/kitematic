Name: kitematic
Version: 0.17.0
Release: 1%{?dist}
Summary: A tool for managing rpm based git projects

Group: Development/Tools
License: GPLv2
URL: https://github.com/RobberPhex/kitematic
Source0: https://github.com/RobberPhex/kitematic/archive/%{version}.zip

BuildRequires: git
BuildRequires: nodejs
BuildRequires: npm

Requires: lsb-core-noarch
Requires: libXss.so.1()(64bit)

%description
Tito is a tool for managing tarballs, rpms, and builds for projects using
git.

%global debug_package %{nil}

%prep
%setup -q -n tito-%{version}

%build
npm install
./node_modules/.bin/grunt clean:release babel less copy:dev shell:linux_npm electron-packager:build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/usr/share/
mkdir -p %{buildroot}/usr/share/pixmaps/
mkdir -p %{buildroot}/usr/share/doc/Kitematic/
mkdir -p %{buildroot}/usr/share/applications/
mkdir -p %{buildroot}/usr/bin/

cp -r dist/Kitematic-linux-x64/ %{buildroot}/usr/share/Kitematic/
ln -sf "../share/Kitematic/Kitematic" "%{buildroot}/usr/bin/Kitematic"

cp util/kitematic.png %{buildroot}/usr/share/pixmaps/Kitematic.png
cp LICENSE %{buildroot}/usr/share/doc/Kitematic/LICENSE
cp resources/linux/Kitematic.desktop %{buildroot}/usr/share/applications/Kitematic.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/bin/Kitematic
/usr/share/Kitematic/
/usr/share/applications/Kitematic.desktop
/usr/share/doc/Kitematic/
/usr/share/pixmaps/Kitematic.png

%changelog
