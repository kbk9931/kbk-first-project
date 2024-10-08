# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: scipy, version: 1.6.2
# Module: scipy.sparse.linalg.eigen.arpack._arpack, version: $Revision: $
import builtins as _mod_builtins
import typing

__doc__: str
__file__: str
__name__: str
__package__: str
__version__: bytes

def cnaupd(
    ido, bmat, which, nev, tol, resid, v, iparam, ipntr, workd, workl, rwork, info, n=..., ncv=..., ldv=..., lworkl=...
) -> typing.Any:
    "ido,tol,resid,v,iparam,ipntr,info = cnaupd(ido,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,rwork,info,[n,ncv,ldv,lworkl])\n\nWrapper for ``cnaupd``.\n\nParameters\n----------\nido : input int\nbmat : input string(len=1)\nwhich : input string(len=2)\nnev : input int\ntol : input float\nresid : input rank-1 array('F') with bounds (n)\nv : input rank-2 array('F') with bounds (ldv,ncv)\niparam : input rank-1 array('i') with bounds (11)\nipntr : input rank-1 array('i') with bounds (14)\nworkd : in/output rank-1 array('F') with bounds (3 * n)\nworkl : in/output rank-1 array('F') with bounds (lworkl)\nrwork : in/output rank-1 array('f') with bounds (ncv)\ninfo : input int\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: len(resid)\nncv : input int, optional\n    Default: shape(v,1)\nldv : input int, optional\n    Default: shape(v,0)\nlworkl : input int, optional\n    Default: len(workl)\n\nReturns\n-------\nido : int\ntol : float\nresid : rank-1 array('F') with bounds (n)\nv : rank-2 array('F') with bounds (ldv,ncv)\niparam : rank-1 array('i') with bounds (11)\nipntr : rank-1 array('i') with bounds (14)\ninfo : int\n"
    ...

def cneupd(
    rvec,
    howmny,
    select,
    sigma,
    workev,
    bmat,
    which,
    nev,
    tol,
    resid,
    v,
    iparam,
    ipntr,
    workd,
    workl,
    rwork,
    info,
    ldz=...,
    n=...,
    ncv=...,
    ldv=...,
    lworkl=...,
) -> typing.Any:
    "d,z,info = cneupd(rvec,howmny,select,sigma,workev,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,rwork,info,[ldz,n,ncv,ldv,lworkl])\n\nWrapper for ``cneupd``.\n\nParameters\n----------\nrvec : input int\nhowmny : input string(len=1)\nselect : input rank-1 array('i') with bounds (ncv)\nsigma : input complex\nworkev : input rank-1 array('F') with bounds (3 * ncv)\nbmat : input string(len=1)\nwhich : input string(len=2)\nnev : input int\ntol : input float\nresid : input rank-1 array('F') with bounds (n)\nv : input rank-2 array('F') with bounds (ldv,ncv)\niparam : input rank-1 array('i') with bounds (11)\nipntr : input rank-1 array('i') with bounds (14)\nworkd : input rank-1 array('F') with bounds (3 * n)\nworkl : input rank-1 array('F') with bounds (lworkl)\nrwork : input rank-1 array('f') with bounds (ncv)\ninfo : input int\n\nOther Parameters\n----------------\nldz : input int, optional\n    Default: shape(z,0)\nn : input int, optional\n    Default: len(resid)\nncv : input int, optional\n    Default: len(select)\nldv : input int, optional\n    Default: shape(v,0)\nlworkl : input int, optional\n    Default: len(workl)\n\nReturns\n-------\nd : rank-1 array('F') with bounds (nev)\nz : rank-2 array('F') with bounds (n,nev)\ninfo : int\n"
    ...

def debug() -> typing.Any:
    "'i'-scalar\n'i'-scalar\n'i'-scalar\n'i'-scalar\n'i'-scalar\n'i'-scalar\n'i'-scalar\n'i'-scalar\n'i'-scalar\n'i'-scalar\n'i'-scalar\n'i'-scalar\n'i'-scalar\n'i'-scalar\n'i'-scalar\n'i'-scalar\n'i'-scalar\n'i'-scalar\n'i'-scalar\n'i'-scalar\n'i'-scalar\n'i'-scalar\n'i'-scalar\n'i'-scalar\n"
    ...

def dnaupd(
    ido, bmat, which, nev, tol, resid, v, iparam, ipntr, workd, workl, info, n=..., ncv=..., ldv=..., lworkl=...
) -> typing.Any:
    "ido,tol,resid,v,iparam,ipntr,info = dnaupd(ido,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,info,[n,ncv,ldv,lworkl])\n\nWrapper for ``dnaupd``.\n\nParameters\n----------\nido : input int\nbmat : input string(len=1)\nwhich : input string(len=2)\nnev : input int\ntol : input float\nresid : input rank-1 array('d') with bounds (n)\nv : input rank-2 array('d') with bounds (ldv,ncv)\niparam : input rank-1 array('i') with bounds (11)\nipntr : input rank-1 array('i') with bounds (14)\nworkd : in/output rank-1 array('d') with bounds (3 * n)\nworkl : in/output rank-1 array('d') with bounds (lworkl)\ninfo : input int\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: len(resid)\nncv : input int, optional\n    Default: shape(v,1)\nldv : input int, optional\n    Default: shape(v,0)\nlworkl : input int, optional\n    Default: len(workl)\n\nReturns\n-------\nido : int\ntol : float\nresid : rank-1 array('d') with bounds (n)\nv : rank-2 array('d') with bounds (ldv,ncv)\niparam : rank-1 array('i') with bounds (11)\nipntr : rank-1 array('i') with bounds (14)\ninfo : int\n"
    ...

def dneupd(
    rvec,
    howmny,
    select,
    sigmar,
    sigmai,
    workev,
    bmat,
    which,
    nev,
    tol,
    resid,
    v,
    iparam,
    ipntr,
    workd,
    workl,
    info,
    ldz=...,
    n=...,
    ncv=...,
    ldv=...,
    lworkl=...,
) -> typing.Any:
    "dr,di,z,info = dneupd(rvec,howmny,select,sigmar,sigmai,workev,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,info,[ldz,n,ncv,ldv,lworkl])\n\nWrapper for ``dneupd``.\n\nParameters\n----------\nrvec : input int\nhowmny : input string(len=1)\nselect : input rank-1 array('i') with bounds (ncv)\nsigmar : input float\nsigmai : input float\nworkev : input rank-1 array('d') with bounds (3 * ncv)\nbmat : input string(len=1)\nwhich : input string(len=2)\nnev : input int\ntol : input float\nresid : input rank-1 array('d') with bounds (n)\nv : input rank-2 array('d') with bounds (n,ncv)\niparam : input rank-1 array('i') with bounds (11)\nipntr : input rank-1 array('i') with bounds (14)\nworkd : input rank-1 array('d') with bounds (3 * n)\nworkl : input rank-1 array('d') with bounds (lworkl)\ninfo : input int\n\nOther Parameters\n----------------\nldz : input int, optional\n    Default: shape(z,0)\nn : input int, optional\n    Default: len(resid)\nncv : input int, optional\n    Default: len(select)\nldv : input int, optional\n    Default: shape(v,0)\nlworkl : input int, optional\n    Default: len(workl)\n\nReturns\n-------\ndr : rank-1 array('d') with bounds (nev + 1)\ndi : rank-1 array('d') with bounds (nev + 1)\nz : rank-2 array('d') with bounds (n,nev + 1)\ninfo : int\n"
    ...

def dsaupd(
    ido, bmat, which, nev, tol, resid, v, iparam, ipntr, workd, workl, info, n=..., ncv=..., ldv=..., lworkl=...
) -> typing.Any:
    "ido,tol,resid,v,iparam,ipntr,info = dsaupd(ido,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,info,[n,ncv,ldv,lworkl])\n\nWrapper for ``dsaupd``.\n\nParameters\n----------\nido : input int\nbmat : input string(len=1)\nwhich : input string(len=2)\nnev : input int\ntol : input float\nresid : input rank-1 array('d') with bounds (n)\nv : input rank-2 array('d') with bounds (ldv,ncv)\niparam : input rank-1 array('i') with bounds (11)\nipntr : input rank-1 array('i') with bounds (11)\nworkd : in/output rank-1 array('d') with bounds (3 * n)\nworkl : in/output rank-1 array('d') with bounds (lworkl)\ninfo : input int\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: len(resid)\nncv : input int, optional\n    Default: shape(v,1)\nldv : input int, optional\n    Default: shape(v,0)\nlworkl : input int, optional\n    Default: len(workl)\n\nReturns\n-------\nido : int\ntol : float\nresid : rank-1 array('d') with bounds (n)\nv : rank-2 array('d') with bounds (ldv,ncv)\niparam : rank-1 array('i') with bounds (11)\nipntr : rank-1 array('i') with bounds (11)\ninfo : int\n"
    ...

def dseupd(
    rvec,
    howmny,
    select,
    sigma,
    bmat,
    which,
    nev,
    tol,
    resid,
    v,
    iparam,
    ipntr,
    workd,
    workl,
    info,
    ldz=...,
    n=...,
    ncv=...,
    ldv=...,
    lworkl=...,
) -> typing.Any:
    "d,z,info = dseupd(rvec,howmny,select,sigma,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,info,[ldz,n,ncv,ldv,lworkl])\n\nWrapper for ``dseupd``.\n\nParameters\n----------\nrvec : input int\nhowmny : input string(len=1)\nselect : input rank-1 array('i') with bounds (ncv)\nsigma : input float\nbmat : input string(len=1)\nwhich : input string(len=2)\nnev : input int\ntol : input float\nresid : input rank-1 array('d') with bounds (n)\nv : input rank-2 array('d') with bounds (ldv,ncv)\niparam : input rank-1 array('i') with bounds (7)\nipntr : input rank-1 array('i') with bounds (11)\nworkd : input rank-1 array('d') with bounds (2 * n)\nworkl : input rank-1 array('d') with bounds (lworkl)\ninfo : input int\n\nOther Parameters\n----------------\nldz : input int, optional\n    Default: shape(z,0)\nn : input int, optional\n    Default: len(resid)\nncv : input int, optional\n    Default: len(select)\nldv : input int, optional\n    Default: shape(v,0)\nlworkl : input int, optional\n    Default: len(workl)\n\nReturns\n-------\nd : rank-1 array('d') with bounds (nev)\nz : rank-2 array('d') with bounds (n,nev)\ninfo : int\n"
    ...

def snaupd(
    ido, bmat, which, nev, tol, resid, v, iparam, ipntr, workd, workl, info, n=..., ncv=..., ldv=..., lworkl=...
) -> typing.Any:
    "ido,tol,resid,v,iparam,ipntr,info = snaupd(ido,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,info,[n,ncv,ldv,lworkl])\n\nWrapper for ``snaupd``.\n\nParameters\n----------\nido : input int\nbmat : input string(len=1)\nwhich : input string(len=2)\nnev : input int\ntol : input float\nresid : input rank-1 array('f') with bounds (n)\nv : input rank-2 array('f') with bounds (ldv,ncv)\niparam : input rank-1 array('i') with bounds (11)\nipntr : input rank-1 array('i') with bounds (14)\nworkd : in/output rank-1 array('f') with bounds (3 * n)\nworkl : in/output rank-1 array('f') with bounds (lworkl)\ninfo : input int\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: len(resid)\nncv : input int, optional\n    Default: shape(v,1)\nldv : input int, optional\n    Default: shape(v,0)\nlworkl : input int, optional\n    Default: len(workl)\n\nReturns\n-------\nido : int\ntol : float\nresid : rank-1 array('f') with bounds (n)\nv : rank-2 array('f') with bounds (ldv,ncv)\niparam : rank-1 array('i') with bounds (11)\nipntr : rank-1 array('i') with bounds (14)\ninfo : int\n"
    ...

def sneupd(
    rvec,
    howmny,
    select,
    sigmar,
    sigmai,
    workev,
    bmat,
    which,
    nev,
    tol,
    resid,
    v,
    iparam,
    ipntr,
    workd,
    workl,
    info,
    ldz=...,
    n=...,
    ncv=...,
    ldv=...,
    lworkl=...,
) -> typing.Any:
    "dr,di,z,info = sneupd(rvec,howmny,select,sigmar,sigmai,workev,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,info,[ldz,n,ncv,ldv,lworkl])\n\nWrapper for ``sneupd``.\n\nParameters\n----------\nrvec : input int\nhowmny : input string(len=1)\nselect : input rank-1 array('i') with bounds (ncv)\nsigmar : input float\nsigmai : input float\nworkev : input rank-1 array('f') with bounds (3 * ncv)\nbmat : input string(len=1)\nwhich : input string(len=2)\nnev : input int\ntol : input float\nresid : input rank-1 array('f') with bounds (n)\nv : input rank-2 array('f') with bounds (n,ncv)\niparam : input rank-1 array('i') with bounds (11)\nipntr : input rank-1 array('i') with bounds (14)\nworkd : input rank-1 array('f') with bounds (3 * n)\nworkl : input rank-1 array('f') with bounds (lworkl)\ninfo : input int\n\nOther Parameters\n----------------\nldz : input int, optional\n    Default: shape(z,0)\nn : input int, optional\n    Default: len(resid)\nncv : input int, optional\n    Default: len(select)\nldv : input int, optional\n    Default: shape(v,0)\nlworkl : input int, optional\n    Default: len(workl)\n\nReturns\n-------\ndr : rank-1 array('f') with bounds (nev + 1)\ndi : rank-1 array('f') with bounds (nev + 1)\nz : rank-2 array('f') with bounds (n,nev + 1)\ninfo : int\n"
    ...

def ssaupd(
    ido, bmat, which, nev, tol, resid, v, iparam, ipntr, workd, workl, info, n=..., ncv=..., ldv=..., lworkl=...
) -> typing.Any:
    "ido,tol,resid,v,iparam,ipntr,info = ssaupd(ido,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,info,[n,ncv,ldv,lworkl])\n\nWrapper for ``ssaupd``.\n\nParameters\n----------\nido : input int\nbmat : input string(len=1)\nwhich : input string(len=2)\nnev : input int\ntol : input float\nresid : input rank-1 array('f') with bounds (n)\nv : input rank-2 array('f') with bounds (ldv,ncv)\niparam : input rank-1 array('i') with bounds (11)\nipntr : input rank-1 array('i') with bounds (11)\nworkd : in/output rank-1 array('f') with bounds (3 * n)\nworkl : in/output rank-1 array('f') with bounds (lworkl)\ninfo : input int\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: len(resid)\nncv : input int, optional\n    Default: shape(v,1)\nldv : input int, optional\n    Default: shape(v,0)\nlworkl : input int, optional\n    Default: len(workl)\n\nReturns\n-------\nido : int\ntol : float\nresid : rank-1 array('f') with bounds (n)\nv : rank-2 array('f') with bounds (ldv,ncv)\niparam : rank-1 array('i') with bounds (11)\nipntr : rank-1 array('i') with bounds (11)\ninfo : int\n"
    ...

def sseupd(
    rvec,
    howmny,
    select,
    sigma,
    bmat,
    which,
    nev,
    tol,
    resid,
    v,
    iparam,
    ipntr,
    workd,
    workl,
    info,
    ldz=...,
    n=...,
    ncv=...,
    ldv=...,
    lworkl=...,
) -> typing.Any:
    "d,z,info = sseupd(rvec,howmny,select,sigma,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,info,[ldz,n,ncv,ldv,lworkl])\n\nWrapper for ``sseupd``.\n\nParameters\n----------\nrvec : input int\nhowmny : input string(len=1)\nselect : input rank-1 array('i') with bounds (ncv)\nsigma : input float\nbmat : input string(len=1)\nwhich : input string(len=2)\nnev : input int\ntol : input float\nresid : input rank-1 array('f') with bounds (n)\nv : input rank-2 array('f') with bounds (ldv,ncv)\niparam : input rank-1 array('i') with bounds (7)\nipntr : input rank-1 array('i') with bounds (11)\nworkd : input rank-1 array('f') with bounds (2 * n)\nworkl : input rank-1 array('f') with bounds (lworkl)\ninfo : input int\n\nOther Parameters\n----------------\nldz : input int, optional\n    Default: shape(z,0)\nn : input int, optional\n    Default: len(resid)\nncv : input int, optional\n    Default: len(select)\nldv : input int, optional\n    Default: shape(v,0)\nlworkl : input int, optional\n    Default: len(workl)\n\nReturns\n-------\nd : rank-1 array('f') with bounds (nev)\nz : rank-2 array('f') with bounds (n,nev)\ninfo : int\n"
    ...

def timing() -> typing.Any:
    "'i'-scalar\n'i'-scalar\n'i'-scalar\n'i'-scalar\n'i'-scalar\n'f'-scalar\n'f'-scalar\n'f'-scalar\n'f'-scalar\n'f'-scalar\n'f'-scalar\n'f'-scalar\n'f'-scalar\n'f'-scalar\n'f'-scalar\n'f'-scalar\n'f'-scalar\n'f'-scalar\n'f'-scalar\n'f'-scalar\n'f'-scalar\n'f'-scalar\n'f'-scalar\n'f'-scalar\n'f'-scalar\n'f'-scalar\n'f'-scalar\n'f'-scalar\n'f'-scalar\n'f'-scalar\n'f'-scalar\n"
    ...

def znaupd(
    ido, bmat, which, nev, tol, resid, v, iparam, ipntr, workd, workl, rwork, info, n=..., ncv=..., ldv=..., lworkl=...
) -> typing.Any:
    "ido,tol,resid,v,iparam,ipntr,info = znaupd(ido,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,rwork,info,[n,ncv,ldv,lworkl])\n\nWrapper for ``znaupd``.\n\nParameters\n----------\nido : input int\nbmat : input string(len=1)\nwhich : input string(len=2)\nnev : input int\ntol : input float\nresid : input rank-1 array('D') with bounds (n)\nv : input rank-2 array('D') with bounds (ldv,ncv)\niparam : input rank-1 array('i') with bounds (11)\nipntr : input rank-1 array('i') with bounds (14)\nworkd : in/output rank-1 array('D') with bounds (3 * n)\nworkl : in/output rank-1 array('D') with bounds (lworkl)\nrwork : in/output rank-1 array('d') with bounds (ncv)\ninfo : input int\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: len(resid)\nncv : input int, optional\n    Default: shape(v,1)\nldv : input int, optional\n    Default: shape(v,0)\nlworkl : input int, optional\n    Default: len(workl)\n\nReturns\n-------\nido : int\ntol : float\nresid : rank-1 array('D') with bounds (n)\nv : rank-2 array('D') with bounds (ldv,ncv)\niparam : rank-1 array('i') with bounds (11)\nipntr : rank-1 array('i') with bounds (14)\ninfo : int\n"
    ...

def zneupd(
    rvec,
    howmny,
    select,
    sigma,
    workev,
    bmat,
    which,
    nev,
    tol,
    resid,
    v,
    iparam,
    ipntr,
    workd,
    workl,
    rwork,
    info,
    ldz=...,
    n=...,
    ncv=...,
    ldv=...,
    lworkl=...,
) -> typing.Any:
    "d,z,info = zneupd(rvec,howmny,select,sigma,workev,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,rwork,info,[ldz,n,ncv,ldv,lworkl])\n\nWrapper for ``zneupd``.\n\nParameters\n----------\nrvec : input int\nhowmny : input string(len=1)\nselect : input rank-1 array('i') with bounds (ncv)\nsigma : input complex\nworkev : input rank-1 array('D') with bounds (3 * ncv)\nbmat : input string(len=1)\nwhich : input string(len=2)\nnev : input int\ntol : input float\nresid : input rank-1 array('D') with bounds (n)\nv : input rank-2 array('D') with bounds (ldv,ncv)\niparam : input rank-1 array('i') with bounds (11)\nipntr : input rank-1 array('i') with bounds (14)\nworkd : input rank-1 array('D') with bounds (3 * n)\nworkl : input rank-1 array('D') with bounds (lworkl)\nrwork : input rank-1 array('d') with bounds (ncv)\ninfo : input int\n\nOther Parameters\n----------------\nldz : input int, optional\n    Default: shape(z,0)\nn : input int, optional\n    Default: len(resid)\nncv : input int, optional\n    Default: len(select)\nldv : input int, optional\n    Default: shape(v,0)\nlworkl : input int, optional\n    Default: len(workl)\n\nReturns\n-------\nd : rank-1 array('D') with bounds (nev)\nz : rank-2 array('D') with bounds (n,nev)\ninfo : int\n"
    ...

def __getattr__(name) -> typing.Any: ...
