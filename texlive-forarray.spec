# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/forarray
# catalog-date 2008-08-19 20:38:14 +0200
# catalog-license lppl
# catalog-version 1.01
Name:		texlive-forarray
Version:	1.01
Release:	10
Summary:	Using array structures in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/forarray
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/forarray.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/forarray.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/forarray.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides functionality for processing lists and
array structures in LaTeX. Arrays can contain characters as
well as TeX and LaTeX commands, nesting of arrays is possible,
and arrays are processed within the same brace level as their
surrounding environment. Array levels can be delimited by
characters or control sequences defined by the user. Practical
uses of this package include data management, construction of
lists and tables, and calculations based on the contents of
lists and arrays.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/forarray/forarray.sty
%doc %{_texmfdistdir}/doc/latex/forarray/README.txt
%doc %{_texmfdistdir}/doc/latex/forarray/forarray
%doc %{_texmfdistdir}/doc/latex/forarray/forarray-test.pdf
%doc %{_texmfdistdir}/doc/latex/forarray/forarray-test.tex
%doc %{_texmfdistdir}/doc/latex/forarray/forarray.dtm
%doc %{_texmfdistdir}/doc/latex/forarray/forarray.dts
%doc %{_texmfdistdir}/doc/latex/forarray/forarray.pdf
#- source
%doc %{_texmfdistdir}/source/latex/forarray/forarray.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.01-2
+ Revision: 752063
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.01-1
+ Revision: 718492
- texlive-forarray
- texlive-forarray
- texlive-forarray
- texlive-forarray

