Name:		texlive-pst-diffraction
Version:	62977
Release:	2
Summary:	Print diffraction patterns from various apertures
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-diffraction
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-diffraction.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-diffraction.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-diffraction.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package enables the user to draw the diffraction patterns
for different geometric forms of apertures for monochromatic
light. The aperture stops can have rectangular, circular or
triangular openings. The view of the diffraction may be planar,
or three-dimensional. Options available are the dimensions of
the aperture under consideration and of the particular optical
setting, e.g. the radius in case of an circular opening.
Moreover one can choose the wavelength of the light (the
associated color will be calculated by the package).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/pst-diffraction/pst-diffraction.tex
%{_texmfdistdir}/tex/latex/pst-diffraction/pst-diffraction.sty
%doc %{_texmfdistdir}/doc/generic/pst-diffraction/Changes
%doc %{_texmfdistdir}/doc/generic/pst-diffraction/README
%doc %{_texmfdistdir}/doc/generic/pst-diffraction/pst-diffraction-doc.bib
%doc %{_texmfdistdir}/doc/generic/pst-diffraction/pst-diffraction-docDE.pdf
%doc %{_texmfdistdir}/doc/generic/pst-diffraction/pst-diffraction-docDE.tex
%doc %{_texmfdistdir}/doc/generic/pst-diffraction/pst-diffraction-docE.pdf
%doc %{_texmfdistdir}/doc/generic/pst-diffraction/pst-diffraction-docE.tex
%doc %{_texmfdistdir}/doc/generic/pst-diffraction/pst-diffraction-docFR.pdf
%doc %{_texmfdistdir}/doc/generic/pst-diffraction/pst-diffraction-docFR.tex
#- source
%doc %{_texmfdistdir}/source/generic/pst-diffraction/Makefile

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
