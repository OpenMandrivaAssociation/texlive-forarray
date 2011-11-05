# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/forarray
# catalog-date 2008-08-19 20:38:14 +0200
# catalog-license lppl
# catalog-version 1.01
Name:		texlive-forarray
Version:	1.01
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

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

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
