import random
import time

NOF_PACKETS = 10

def arc4rand(a):
    """
    Mimics the custom random number generator from the C code.
    Ensures the value is non-zero.
    """
    # Generates a pseudo-random value similar to (rand() % 10) % a
    rn = (random.randint(0, 99) % 10) % a
    return 1 if rn == 0 else rn

def main():
    p_sz_rm = 0  # Packet size remaining in the bucket
    packet_sz = []

    # Initialize packet sizes randomly
    for _ in range(NOF_PACKETS):
        # Generates sizes like 10, 20, 30, 40, 50 bytes
        packet_sz.append(arc4rand(6) * 10)

    # Display generated packets
    for i in range(NOF_PACKETS):
        print(f"packet[{i}]: {packet_sz[i]} bytes")

    # User Inputs
    o_rate = int(input("\nEnter the Output rate: "))
    b_size = int(input("Enter the Bucket Size: "))

    # Process each packet
    for i in range(NOF_PACKETS):
        if packet_sz[i] + p_sz_rm > b_size:
            if packet_sz[i] > b_size:
                print(f"\nIncoming packet size ({packet_sz[i]} bytes) is Greater than bucket capacity ({b_size} bytes)-PACKET REJECTED")
            else:
                print("\nBucket capacity exceeded-PACKETS REJECTED!!")
        else:
            p_sz_rm += packet_sz[i]
            print(f"\nIncoming Packet size: {packet_sz[i]}")
            print(f"Bytes remaining to Transmit: {p_sz_rm}")
           
            p_time = arc4rand(4) * 10
            print(f"Time left for transmission: {p_time} units")

            # Leak/Transmission simulation loop over time clock
            for clk in range(10, p_time + 1, 10):
                time.sleep(1)  # Delay of 1 second per clock cycle
               
                if p_sz_rm > 0:
                    if p_sz_rm <= o_rate:
                        op = p_sz_rm
                        p_sz_rm = 0
                    else:
                        op = o_rate
                        p_sz_rm -= o_rate
                   
                    print(f"\nPacket of size {op} Transmitted")
                    print(f"Bytes Remaining to Transmit: {p_sz_rm}")
                else:
                    print(f"\nTime left for transmission: {p_time - clk} units")
                    print("No packets to transmit!!")

if __name__ == "__main__":
    main()
