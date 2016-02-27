%define		kdeframever	5.19
%define		qtver		5.3.2
%define		kfname		kimageformats

Summary:	Image format plugins for Qt
Name:		kf5-%{kfname}
Version:	5.19.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	678b42ebec88ce18ac0c85d539fada01
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
BuildRequires:	kf5-extra-cmake-modules >= 1.0.0
BuildRequires:	libjpeg-devel
BuildRequires:	qt5-linguist >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
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
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
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
%attr(755,root,root) %{qt5dir}/plugins/imageformats/kimg_eps.so
%attr(755,root,root) %{qt5dir}/plugins/imageformats/kimg_exr.so
%attr(755,root,root) %{qt5dir}/plugins/imageformats/kimg_kra.so
%attr(755,root,root) %{qt5dir}/plugins/imageformats/kimg_ora.so
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
%{_datadir}/kservices5/qimageioplugins/kra.desktop
%{_datadir}/kservices5/qimageioplugins/ora.desktop
%{_datadir}/kservices5/qimageioplugins/pcx.desktop
%{_datadir}/kservices5/qimageioplugins/pic.desktop
%{_datadir}/kservices5/qimageioplugins/psd.desktop
%{_datadir}/kservices5/qimageioplugins/ras.desktop
%{_datadir}/kservices5/qimageioplugins/rgb.desktop
%{_datadir}/kservices5/qimageioplugins/tga.desktop
%{_datadir}/kservices5/qimageioplugins/xcf.desktop
