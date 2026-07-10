%global tl_name forarray
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.01
Release:	%{tl_revision}.1
Summary:	Using array structures in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/forarray
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/forarray.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/forarray.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/forarray.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides functionality for processing lists and array
structures in LaTeX. Arrays can contain characters as well as TeX and
LaTeX commands, nesting of arrays is possible, and arrays are processed
within the same brace level as their surrounding environment. Array
levels can be delimited by characters or control sequences defined by
the user. Practical uses of this package include data management,
construction of lists and tables, and calculations based on the contents
of lists and arrays.

