Name: ruya-backgrounds
Version: 2
Release: 1%{?dist}
Summary: Ruya backgrounds
Summary(ar): خلفيات رؤية
License: GPLv2
URL: https://parmg.sa
Source0: gpl-2.0.txt
Source1: ruya-bg-001-v3.jpg

Source100: ruya.xml
Source101: metadata.desktop

BuildArch: noarch

%description
Ruya backgrounds

%description -l ar
خلفيات رؤية

%prep
cp %{SOURCE0} .

%install
mkdir -p %{buildroot}%{_datadir}/backgrounds/RUYA
mkdir -p %{buildroot}%{_datadir}/gnome-background-properties

install -Dp -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/backgrounds/RUYA
install -Dp -m 0644 %{SOURCE100} %{buildroot}%{_datadir}/gnome-background-properties

mkdir -p %{buildroot}%{_datadir}/wallpapers/RUYA/contents/images
mkdir -p %{buildroot}%{_datadir}/plasma/desktoptheme/RUYA

ln -s %{_datadir}/backgrounds/RUYA/ruya-bg-001-v3.jpg %{buildroot}%{_datadir}/wallpapers/RUYA/contents/images/8000x4500

install -Dp -m 0644 %{SOURCE101} %{buildroot}%{_datadir}/plasma/desktoptheme/RUYA
install -Dp -m 0644 %{SOURCE101} %{buildroot}%{_datadir}/wallpapers/RUYA

%files
%license gpl-2.0.txt
%{_datadir}/backgrounds/RUYA/*
%{_datadir}/gnome-background-properties/ruya.xml
%{_datadir}/wallpapers/RUYA/contents/images/*
%{_datadir}/plasma/desktoptheme/RUYA/metadata.desktop
%{_datadir}/wallpapers/RUYA/metadata.desktop

%changelog
* Mon Oct 10 2022 Mosaab Alzoubi <mosaab[AT]parmg[DOT]sa> - 2-1
- Add KDE support

* Thu Mar 24 2022 Mosaab Alzoubi <mosaab[AT]parmg[DOT]sa> - 1.0-5
- Initial
