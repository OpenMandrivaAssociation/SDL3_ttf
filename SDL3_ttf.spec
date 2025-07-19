%define major 0
%define libname %mklibname %{name}
%define devname %mklibname %{name} -d
%global _disable_rebuild_configure 1
#define _disable_lto 1

Summary:	Simple DirectMedia Layer 3 - Sample TrueType Font Library
Name:		SDL3_ttf
Version:	3.2.2
Release:	1
License:	Zlib
Group:		System/Libraries
Url:		https://www.libsdl.org/projects/SDL3_ttf/
Source0:	https://github.com/libsdl-org/SDL3_ttf/releases/download/release-%{version}/SDL3_ttf-%{version}.tar.gz

BuildRequires:	pkgconfig(sdl3)
BuildRequires:	pkgconfig(freetype2)

%description
This is a sample library which allows you to use TrueType fonts in your SDL3
applications.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Main library for %{name}
Group:		System/Libraries

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with %{name}.

%files -n %{libname}
%{_libdir}/libSDL3_ttf.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%files -n %{devname}
#doc README.txt CHANGES.txt
%license %{_datadir}/licenses/SDL3_ttf/LICENSE.txt
%{_includedir}/SDL3_ttf/
%{_libdir}/libSDL3_ttf.so
%{_libdir}/pkgconfig/sdl3-ttf.pc
%{_libdir}/cmake/SDL3_ttf/
%{_mandir}/man3/SDL_*
%{_mandir}/man3/TTF*

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%cmake  \
            -DSDLTTF_HARFBUZZ:BOOL=ON \
            -DSDLTTF_INSTALL:BOOL=ON \
            -DSDLTTF_INSTALL_CPACK:BOOL=ON \
            -DSDLTTF_INSTALL_MAN:BOOL=ON \
            -DSDLTTF_PLUTOSVG:BOOL=OFF \
            -DSDLTTF_RELOCATABLE:BOOL=OFF \
            -DSDLTTF_SAMPLES:BOOL=OFF \
            -DSDLTTF_SAMPLES_INSTALL:BOOL=OFF \
            -DSDLTTF_STRICT:BOOL=ON \
            -DSDLTTF_VENDORED:BOOL=OFF \
            -DSDLTTF_WERROR:BOOL=OFF
	
 
%make_build

%install
%make_install -C build
