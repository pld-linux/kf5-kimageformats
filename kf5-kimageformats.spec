# TODO:
# - dir /usr/share/kservices5 not packaged
%define         _state          stable
%define		orgname		kimageformats

Summary:	Image format plugins for Qt
Name:		kf5-%{orgname}
Version:	5.0.0
Release:	0.1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/frameworks/%{version}/%{orgname}-%{version}.tar.xz
# Source0-md5:	333084e7efc1efaa74c4008aec895ada
URL:		http://www.kde.org/
BuildRequires:	OpenEXR-devel
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Gui-devel >= 5.3.1
BuildRequires:	Qt5PrintSupport-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5Widgets-devel >= 5.3.1
BuildRequires:	Qt5X11Extras-devel >= 5.2.0
BuildRequires:	cmake >= 2.8.12
BuildRequires:	jasper-devel
BuildRequires:	kf5-extra-cmake-modules >= 1.0.0
BuildRequires:	libjpeg-devel
BuildRequires:	qt5-linguist
BuildRequires:	rpmbuild(macros) >= 1.164
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
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	-DBIN_INSTALL_DIR=%{_bindir} \
	-DKCFG_INSTALL_DIR=%{_datadir}/config.kcfg \
	-DPLUGIN_INSTALL_DIR=%{qt5dir}/plugins \
	-DQT_PLUGIN_INSTALL_DIR=%{qt5dir}/plugins \
	-DQML_INSTALL_DIR=%{qt5dir}/qml \
	-DIMPORTS_INSTALL_DIR=%{qt5dirs}/imports \
	-DSYSCONF_INSTALL_DIR=%{_sysconfdir} \
	-DLIBEXEC_INSTALL_DIR=%{_libexecdir} \
	-DKF5_LIBEXEC_INSTALL_DIR=%{_libexecdir} \
	-DKF5_INCLUDE_INSTALL_DIR=%{_includedir} \
	-DECM_MKSPECS_INSTALL_DIR=%{qt5dir}/mkspecs/modules \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{qt5dir}/plugins/imageformats/kimg_dds.so
%attr(755,root,root) %{qt5dir}/plugins/imageformats/kimg_eps.so
%attr(755,root,root) %{qt5dir}/plugins/imageformats/kimg_exr.so
%attr(755,root,root) %{qt5dir}/plugins/imageformats/kimg_jp2.so
%attr(755,root,root) %{qt5dir}/plugins/imageformats/kimg_pcx.so
%attr(755,root,root) %{qt5dir}/plugins/imageformats/kimg_pic.so
%attr(755,root,root) %{qt5dir}/plugins/imageformats/kimg_psd.so
%attr(755,root,root) %{qt5dir}/plugins/imageformats/kimg_ras.so
%attr(755,root,root) %{qt5dir}/plugins/imageformats/kimg_rgb.so
%attr(755,root,root) %{qt5dir}/plugins/imageformats/kimg_tga.so
%attr(755,root,root) %{qt5dir}/plugins/imageformats/kimg_xcf.so
%dir %{_datadir}/kservices5/qimageioplugins
%{_datadir}/kservices5/qimageioplugins/dds.desktop
%{_datadir}/kservices5/qimageioplugins/eps.desktop
%{_datadir}/kservices5/qimageioplugins/exr.desktop
%{_datadir}/kservices5/qimageioplugins/jp2.desktop
%{_datadir}/kservices5/qimageioplugins/pcx.desktop
%{_datadir}/kservices5/qimageioplugins/pic.desktop
%{_datadir}/kservices5/qimageioplugins/psd.desktop
%{_datadir}/kservices5/qimageioplugins/ras.desktop
%{_datadir}/kservices5/qimageioplugins/rgb.desktop
%{_datadir}/kservices5/qimageioplugins/tga.desktop
%{_datadir}/kservices5/qimageioplugins/xcf.desktop
