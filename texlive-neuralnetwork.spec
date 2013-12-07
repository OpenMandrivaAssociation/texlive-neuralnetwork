# revision 31500
# category Package
# catalog-ctan /graphics/pgf/contrib/neuralnetwork
# catalog-date 2013-08-22 18:53:49 +0200
# catalog-license gpl
# catalog-version 1.0
Name:		texlive-neuralnetwork
Version:	1.0
Release:	3
Summary:	Graph-drawing for neural networks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/neuralnetwork
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/neuralnetwork.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/neuralnetwork.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides facilities for graph-drawing, with
facilities designed for neural network diagrams.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/neuralnetwork/neuralnetwork.sty
%doc %{_texmfdistdir}/doc/latex/neuralnetwork/examples/neural-networks-ebook.pdf
%doc %{_texmfdistdir}/doc/latex/neuralnetwork/examples/neuralnetwork.pdf
%doc %{_texmfdistdir}/doc/latex/neuralnetwork/examples/neuralnetwork.tex
%doc %{_texmfdistdir}/doc/latex/neuralnetwork/examples/xor.pdf
%doc %{_texmfdistdir}/doc/latex/neuralnetwork/examples/xor.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
