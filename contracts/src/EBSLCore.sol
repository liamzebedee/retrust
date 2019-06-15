pragma solidity ^0.5.6;

contract EBSLCore {
  function opinion_add ( uint168[3] memory x, uint168[3] memory y ) public returns ( uint168[3] memory out );
  function opinion_scalar_mult ( uint168 a, uint168[3] memory x ) public returns ( uint168[3] memory out );
  function opinion_generic_discount ( uint168[3] memory x, uint168[3] memory y ) public returns ( uint168[3] memory out );
  function evidence_transfer_scalar ( uint168[3] memory x ) public returns ( uint168 out );
  function to_opinion (int128 evidence) public returns ( uint168[3] memory out );
  function check_xtol ( uint168 a1, uint168 a2 ) external returns ( bool out );
}