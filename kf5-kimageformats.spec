#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeframever	5.98
%define		qtver		5.15.2
%define		kfname		kimageformats

Summary:	Image format plugins for Qt
Name:		kf5-%{kfname}
Version:	5.98.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	602b5722184c84d8167c5927f5310014
URL:		http://www.kde.org/
BuildRequires:	OpenEXR-devel
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5PrintSupport-devel >= %{qtver}
BuildRequires:	Qt5Test-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	Qt5X11Extras-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= %{version}
BuildRequires:	libavif-devel >= 0.8.2
BuildRequires:	libjpeg-devel
BuildRequires:	libjxl-devel
BuildRequires:	ninja
BuildRequires:	qt5-linguist >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	kf5-dirs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
This framework provides additional image format plugins for QtGui. As
such it is not required for the compilation of any other software, but
may be a runtime requirement for Qt-based software to support certain
image formats.

The following image formats have read-only support:

- DirectDraw Surface (dds)
- Gimp (xcf)
- OpenEXR (exr)
- Photoshop documents (psd)
- Sun Raster (ras)

The following image formats have read and write support:

- Encapsulated PostScript (eps)
- JPEG-2000 (jp2)
- Personal Computer Exchange (pcx)
- SGI images (rgb, rgba, sgi, bw)
- Softimage PIC (pic)
- Targa (tga): supports more formats than Qt's version
- XView (xv)

%prep
%setup -q -n %{kfname}-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%ninja_build

%if %{with tests}
ctest
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{qt5dir}/plugins/imageformats/kimg_avif.so
%attr(755,root,root) %{qt5dir}/plugins/imageformats/kimg_hdr.so
%attr(755,root,root) %{qt5dir}/plugins/imageformats/kimg_eps.so
%attr(755,root,root) %{qt5dir}/plugins/imageformats/kimg_exr.so
%attr(755,root,root) %{qt5dir}/plugins/imageformats/kimg_jxl.so
%attr(755,root,root) %{qt5dir}/plugins/imageformats/kimg_kra.so
%attr(755,root,root) %{qt5dir}/plugins/imageformats/kimg_ora.so
%attr(755,root,root) %{qt5dir}/plugins/imageformats/kimg_pcx.so
%attr(755,root,root) %{qt5dir}/plugins/imageformats/kimg_pic.so
%attr(755,root,root) %{qt5dir}/plugins/imageformats/kimg_psd.so
%attr(755,root,root) %{qt5dir}/plugins/imageformats/kimg_ras.so
%attr(755,root,root) %{qt5dir}/plugins/imageformats/kimg_rgb.so
%attr(755,root,root) %{qt5dir}/plugins/imageformats/kimg_tga.so
%attr(755,root,root) %{qt5dir}/plugins/imageformats/kimg_xcf.so
%attr(755,root,root) %{_libdir}/qt5/plugins/imageformats/kimg_ani.so
%dir %{_datadir}/kservices5/qimageioplugins
%{_datadir}/kservices5/qimageioplugins/ani.desktop
%{_datadir}/kservices5/qimageioplugins/avif.desktop
%{_datadir}/kservices5/qimageioplugins/hdr.desktop
%{_datadir}/kservices5/qimageioplugins/dds.desktop
%{_datadir}/kservices5/qimageioplugins/eps.desktop
%{_datadir}/kservices5/qimageioplugins/exr.desktop
%{_datadir}/kservices5/qimageioplugins/jp2.desktop
%{_datadir}/kservices5/qimageioplugins/jxl.desktop
%{_datadir}/kservices5/qimageioplugins/kra.desktop
%{_datadir}/kservices5/qimageioplugins/ora.desktop
%{_datadir}/kservices5/qimageioplugins/pcx.desktop
%{_datadir}/kservices5/qimageioplugins/pic.desktop
%{_datadir}/kservices5/qimageioplugins/psd.desktop
%{_datadir}/kservices5/qimageioplugins/ras.desktop
%{_datadir}/kservices5/qimageioplugins/rgb.desktop
%{_datadir}/kservices5/qimageioplugins/tga.desktop
%{_datadir}/kservices5/qimageioplugins/xcf.desktop
